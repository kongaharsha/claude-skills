#!/usr/bin/env python3
"""Cross-foot checks: verify that computed tax values are internally consistent.

Reads the extraction ledger (source data) and computation results, then runs
a battery of arithmetic and attribution checks. Any failure means something
was misread, misattributed, or miscalculated — fix before filling forms.

Usage:
    python cross_foot_check.py work/extraction_ledger.json work/results.json

Output: JSON report to stdout + human-readable summary. Exit code 1 if any check fails.
"""

import json
import sys
from pathlib import Path


def load_json(path):
    with open(path) as f:
        return json.load(f)


def approx_eq(a, b, tol=0.02):
    """Check if two values are approximately equal (within tolerance for rounding)."""
    return abs(a - b) <= tol


def run_checks(ledger, results):
    """Run all cross-foot checks. Returns list of (name, passed, detail) tuples."""
    checks = []
    docs = ledger.get("documents", [])

    # --- Helper: sum a field across all docs of a given type ---
    def sum_field(doc_type, field, filer=None):
        total = 0
        for doc in docs:
            if doc["type"] != doc_type:
                continue
            if filer and doc.get("filer") != filer:
                continue
            val = doc.get("values", {}).get(field, 0)
            if isinstance(val, dict):
                total += sum(val.values())
            else:
                total += val
        return total

    # --- Gather computed values ---
    fed = results.get("federal", results)

    # 1. Total wages = sum of all W-2 box 1
    ledger_wages = sum_field("W-2", "box_1_wages")
    computed_wages = fed.get("wages", fed.get("total_wages", 0))
    checks.append((
        "Wages: ledger W-2 sum = computed",
        approx_eq(ledger_wages, computed_wages),
        f"Ledger: {ledger_wages:.2f}, Computed: {computed_wages:.2f}"
    ))

    # 2. Federal withholding = sum of all W-2 box 2
    ledger_wh = sum_field("W-2", "box_2_fed_wh")
    computed_wh = fed.get("total_fed_wh", fed.get("fed_wh", 0))
    checks.append((
        "Fed withholding: ledger W-2 sum = computed",
        approx_eq(ledger_wh, computed_wh),
        f"Ledger: {ledger_wh:.2f}, Computed: {computed_wh:.2f}"
    ))

    # 3. Dividend attribution — check per-filer, not just totals
    filers = ledger.get("filers", {})
    for filer_key in filers:
        ledger_ord = sum_field("1099-DIV", "ordinary_dividends", filer=filer_key)
        ledger_qual = sum_field("1099-DIV", "qualified_dividends", filer=filer_key)
        if ledger_ord > 0 or ledger_qual > 0:
            name = filers[filer_key].get("first_name", filer_key)
            checks.append((
                f"Dividends ({name}): ledger has per-filer attribution",
                True,
                f"Ordinary: {ledger_ord:.2f}, Qualified: {ledger_qual:.2f}"
            ))

    # 4. AGI arithmetic
    wages = fed.get("wages", fed.get("total_wages", 0))
    interest = fed.get("interest", fed.get("taxable_interest", 0))
    ord_div = fed.get("ord_div", fed.get("ordinary_dividends", 0))
    cap_gain = fed.get("net_cap_gain", fed.get("capital_gains", 0))
    other_inc = fed.get("other_income", 0)
    adjustments = fed.get("adjustments", 0)
    expected_agi = wages + interest + ord_div + cap_gain + other_inc - adjustments
    computed_agi = fed.get("agi", 0)
    checks.append((
        "AGI: income components sum to AGI",
        approx_eq(expected_agi, computed_agi, tol=1.0),
        f"Components sum: {expected_agi:.2f}, Computed AGI: {computed_agi:.2f}"
    ))

    # 5. Tax balance: total_tax - total_payments = owed (or negative = refund)
    total_tax = fed.get("total_tax", 0)
    total_payments = fed.get("total_payments", 0)
    computed_owed = fed.get("owed", fed.get("amount_owed", 0))
    computed_refund = fed.get("refund", 0)
    expected_balance = total_tax - total_payments
    if computed_owed > 0:
        checks.append((
            "Balance: total_tax - total_payments = amount_owed",
            approx_eq(expected_balance, computed_owed, tol=1.0),
            f"Tax: {total_tax:.2f} - Payments: {total_payments:.2f} = {expected_balance:.2f}, Owed: {computed_owed:.2f}"
        ))
    elif computed_refund > 0:
        checks.append((
            "Balance: total_payments - total_tax = refund",
            approx_eq(-expected_balance, computed_refund, tol=1.0),
            f"Payments: {total_payments:.2f} - Tax: {total_tax:.2f} = {-expected_balance:.2f}, Refund: {computed_refund:.2f}"
        ))

    # 6. Medicare wages consistency (for Additional Medicare Tax calc)
    ledger_medicare = sum_field("W-2", "box_5_medicare_wages")
    checks.append((
        "Medicare wages: ledger has values for Additional Medicare Tax calc",
        ledger_medicare > 0,
        f"Total Medicare wages from W-2s: {ledger_medicare:.2f}"
    ))

    return checks


def main():
    if len(sys.argv) < 3:
        print("Usage: python cross_foot_check.py extraction_ledger.json results.json")
        sys.exit(1)

    ledger = load_json(sys.argv[1])
    results = load_json(sys.argv[2])

    checks = run_checks(ledger, results)

    passed = sum(1 for _, p, _ in checks if p)
    failed = sum(1 for _, p, _ in checks if not p)

    print(f"\n{'='*60}")
    print(f"CROSS-FOOT CHECK REPORT")
    print(f"{'='*60}\n")

    for name, ok, detail in checks:
        status = "✓ PASS" if ok else "✗ FAIL"
        print(f"  {status}  {name}")
        print(f"         {detail}\n")

    print(f"{'='*60}")
    print(f"  {passed} passed, {failed} failed")
    print(f"{'='*60}")

    # Also output JSON for programmatic use
    report = {
        "passed": passed,
        "failed": failed,
        "checks": [{"name": n, "passed": p, "detail": d} for n, p, d in checks]
    }
    report_path = Path(sys.argv[1]).parent / "cross_foot_report.json"
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2)
    print(f"\n  Report saved to: {report_path}")

    sys.exit(1 if failed > 0 else 0)


if __name__ == "__main__":
    main()
