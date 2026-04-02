# Platform UI Automation Patterns

Guidance for driving tax filing platforms through browser automation. These patterns come from real filing sessions and address the specific quirks of single-page applications (SPAs) that most modern tax platforms use.

---

## General Principles

### 1. JavaScript injection over simulated clicks

Modern tax platforms are React/Angular SPAs where simulated mouse clicks don't always register, especially on dropdowns and custom inputs. Default to JavaScript for setting values:

```javascript
// Text input
const el = document.querySelector('input[name="fieldName"]');
el.value = 'new value';
el.dispatchEvent(new Event('input', { bubbles: true }));
el.dispatchEvent(new Event('change', { bubbles: true }));

// Select/dropdown
const select = document.querySelector('select[name="fieldName"]');
select.value = 'optionValue';
select.dispatchEvent(new Event('change', { bubbles: true }));

// Radio button
const radio = document.querySelector('input[type="radio"][value="yes"]');
radio.checked = true;
radio.dispatchEvent(new Event('change', { bubbles: true }));

// Checkbox
const cb = document.querySelector('input[type="checkbox"][name="field"]');
cb.checked = true;
cb.dispatchEvent(new Event('change', { bubbles: true }));
```

The `{ bubbles: true }` is critical — without it, React's synthetic event system won't pick up the change.

Fall back to mouse clicks for:
- Custom UI components that don't use standard HTML form elements
- Buttons (Save, Continue, Add) — these usually work fine with clicks
- Navigation links

### 2. Wait for page transitions

SPAs load content dynamically. After clicking "Continue" or navigating:
- Wait 3-5 seconds for the new page to load
- Take a screenshot to confirm you're on the expected page
- If the page hasn't loaded, wait another 2-3 seconds

### 3. Use element references over coordinates

When possible, use accessibility-tree element references (`ref_123`) rather than x/y coordinates. Coordinates shift with window size, zoom level, and dynamic content. Element refs are stable.

### 4. Dismiss blocking overlays first

Before interacting with any page, check for and dismiss:
- Session timeout dialogs ("Are you still there?")
- Maintenance alerts
- Cookie consent banners
- Loading spinners or overlays

---

## FreeTaxUSA-Specific Patterns

### Navigation structure

FreeTaxUSA's top nav bar has dropdown menus. Click the section name to open its dropdown, then click the specific page:

```
Personal > Income > Deductions/Credits > Misc > Summary > State > Final Steps
```

The **State** dropdown has tabs for each state (e.g., "NEW JERSEY" / "NEW YORK") with sub-pages listed under each. Click the state tab first, then the specific page.

**Use these dropdowns to jump directly to any page** rather than clicking "Save and Continue" through intermediate pages.

### Dropdown/select elements

FreeTaxUSA dropdowns are standard HTML `<select>` elements styled with React. They require the change event to register:

```javascript
const select = document.querySelector('select[name="stateDropdown"]');
select.value = '32'; // NY = 32, NJ = 30, etc.
select.dispatchEvent(new Event('change', { bubbles: true }));
```

Direct click interaction with dropdowns is unreliable — use JS.

### Session timeout

FreeTaxUSA shows an "Are you still there?" dialog after ~15 minutes of inactivity. It has a "Continue" button and a countdown timer. Click "Continue" to dismiss it. The platform auto-saves, so no data is lost.

Before every page interaction, check for this dialog and dismiss it if present.

### Page load timing

After clicking "Save and Continue" or a nav link:
- Wait 4-5 seconds for the page to load
- Some pages (especially state returns) take longer
- If the page title hasn't changed after 5 seconds, try clicking again

### Common field patterns

**Yes/No radio buttons**: Usually `<input type="radio" value="Y">` and `<input type="radio" value="N">`. Use JS to set them.

**Currency fields**: Enter numbers without dollar signs or commas. FreeTaxUSA formats them automatically.

**SSN fields**: Enter as 9 digits, no dashes. The platform may split them into three fields (3-2-4 format).

**Date fields**: Usually MM/DD/YYYY format. Some may be separate month/day/year dropdowns.

---

## Other Platforms (Notes)

### TurboTax
- Heavy use of custom UI components — may require more click-based interaction
- Interview-style flow; less direct navigation
- Look for "Jump to" or search features to skip sections

### H&R Block Online
- Similar SPA architecture to FreeTaxUSA
- Navigation sidebar allows direct page access
- May have different field naming conventions

### TaxAct
- Navigation menu with section links
- Standard form-based entry
- Similar JS injection patterns should work

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Click doesn't register on a button | Use element ref instead of coordinates; or use JS `element.click()` |
| Dropdown value doesn't stick | Dispatch both `input` and `change` events with `bubbles: true` |
| Page doesn't advance after clicking Continue | Wait longer (5-7 seconds); check for validation errors on the page |
| Session expired | Navigate back to the login page; the platform auto-saves so you can resume |
| Field is pre-populated with wrong value | Clear the field first with JS before setting the new value |
| Radio button appears selected but form doesn't recognize it | Dispatch `change` event after setting `checked = true` |
