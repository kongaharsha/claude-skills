---
name: make-executive-memo
description: Draft, restructure, critique, or convert notes into Harsha/WK-style executive memos, ELT decision memos, strategy north-star memos, transformation proposals, governance redesign memos, portfolio rationalization memos, and competitive intelligence memos. Use when Codex is asked to make a memo, ELT memo, executive strategy memo, board/leadership note, decision memo, north star narrative, or polished senior-leadership writeup from notes, decks, documents, transcripts, or rough bullets.
---

# Make Executive Memo

## Overview

Create concise, senior-leadership-ready memos in Harsha's WK style: clear purpose, sharp strategic context, explicit implications, decision-led recommendations, and concrete next steps. Use the memo patterns in `references/memo-patterns.md` when a request involves a memo structure, tone, or rewrite.

## Workflow

1. **Clarify the memo job**
   - Identify audience: ELT, CEO, divisional CEO, board, internal strategy team, or external partner.
   - Identify memo type: strategy north star, ELT decision memo, transformation proposal, governance/process redesign, portfolio action, competitive update, or short executive note.
   - Identify required decision: align, approve, choose scope, fund, nominate owners, launch a program, or inform discussion.

2. **Extract the raw material**
   - Pull the problem statement, strategic context, evidence, recommendation, decisions needed, risks, and next steps.
   - If working from `.docx` templates or source documents, use `scripts/extract_docx_outline.py` to quickly inspect headings, paragraphs, and table samples.
   - Do not invent metrics, commitments, owners, dates, or decision rights. Use placeholders only when the missing value is essential.

3. **Select the memo pattern**
   - Read `references/memo-patterns.md` for the relevant pattern and section sequence.
   - Use a decision-led ELT memo for most senior internal requests.
   - Use a north-star memo when the output needs to define a future strategic position.
   - Use a transformation memo when the output asks leadership to launch or align on a change program.

4. **Draft in Harsha/WK style**
   - Start with purpose and the decision the memo seeks.
   - Keep paragraphs tight: usually 2-4 sentences.
   - Use concrete business language: "what is changing," "why it matters," "what we should do," and "what decisions unlock next steps."
   - Prefer named sections over clever headings.
   - Bold sparingly for the ask, recommendation, and major decisions when useful.

5. **Quality check**
   - The first page should answer: why this matters, what is being recommended, and what decision is needed.
   - Every section should earn its place by moving the leader toward a decision.
   - Remove generic strategy language, repeated claims, and unsupported adjectives.
   - Check that the memo separates facts, judgments, and recommendations.

## Output Defaults

- If the user asks for a draft, provide the memo directly.
- If the user asks to restructure an existing memo, preserve the facts and rewrite the structure.
- If the user asks for feedback, lead with the highest-impact edits and then provide revised language.
- If creating a `.docx`, preserve a simple professional document structure unless the user provides a specific template.

## Resources

- `references/memo-patterns.md`: WK memo structures, style rules, common language patterns, and source-template notes.
- `scripts/extract_docx_outline.py`: quick extractor for DOCX paragraphs and table samples.
