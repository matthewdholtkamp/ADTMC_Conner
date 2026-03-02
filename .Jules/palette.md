## 2026-02-19 - Accessibility Retrofit for Multi-State Icons
**Learning:** When retrofitting accessibility onto a legacy codebase where a `div` acts as a multi-state button (e.g., transitioning between Menu/Back/Close icons), static `aria-label`s are insufficient. The label must be updated dynamically in the JavaScript logic that controls the visual state change to ensure screen readers announce the current function, not just the initial one.
**Action:** Always pair visual state transition functions (like `showMenu`, `showArrow`) with a corresponding `setAttribute('aria-label', ...)` call.

## 2026-02-20 - Retrofitting Non-Semantic Buttons
**Learning:** The application heavily relies on `div` elements with classes like `.catbtn` and `.medbtn` for interactivity, lacking native keyboard support. Retrofitting these with `role="button"` and `tabindex="0"` via a centralized JavaScript initializer proved more efficient and less invasive than rewriting thousands of lines of HTML.
**Action:** When facing large legacy codebases with widespread non-semantic interactive elements, use a centralized JS function to inject accessibility attributes and keyboard listeners on load, rather than refactoring the markup component by component.

## 2026-02-21 - Accessible Dynamic Content
**Learning:** `initializeAccessibility` runs only on DOMContentLoaded, missing dynamically generated elements like search results. These elements require explicit injection of accessibility attributes (`role`, `tabindex`) and event listeners (`keydown`) at the time of creation.
**Action:** When creating interactive elements via JavaScript (e.g., in a loop), always attach accessibility attributes and keyboard handlers immediately, rather than relying on a global initializer that runs once on load.

## 2026-02-22 - Taming Verbose Search Results
**Learning:** Adding `aria-live="polite"` to a search results container causes screen readers to read *all* appended items, which is overwhelming for long lists.
**Action:** Dynamically apply `aria-live="polite"` *only* when displaying status messages (like "No results found"), and remove the attribute when displaying the actual result list, relying on `role="listbox"` semantics for the items instead.

## 2026-02-23 - Skip to Content for Keyboard Users
**Learning:** Large monolithic pages with sticky headers or extensive navigation need a "Skip to Content" link to prevent keyboard fatigue. Adding `tabindex="-1"` to the target container is essential for the focus to actually move and stick in some browsers/contexts.
**Action:** Always add `tabindex="-1"` to the target of a skip link if it is not an inherently focusable element.

## 2026-03-01 - Interactive Element States for Screen Readers
**Learning:** For screen readers to accurately represent the UI, toggleable interactive elements like accordions (`.contbox-top`) and disclosure buttons (`.dispo-icon`) must utilize the `aria-expanded` attribute. Its value must be kept in sync with the element's actual visual state via JavaScript (`true` when open, `false` when closed).
**Action:** When creating or modifying toggleable components, ensure `aria-expanded` is initialized properly on load and dynamically updated within the component's state-toggling logic (event listeners).
