## 2026-02-19 - Accessibility Retrofit for Multi-State Icons
**Learning:** When retrofitting accessibility onto a legacy codebase where a `div` acts as a multi-state button (e.g., transitioning between Menu/Back/Close icons), static `aria-label`s are insufficient. The label must be updated dynamically in the JavaScript logic that controls the visual state change to ensure screen readers announce the current function, not just the initial one.
**Action:** Always pair visual state transition functions (like `showMenu`, `showArrow`) with a corresponding `setAttribute('aria-label', ...)` call.

## 2026-02-20 - Retrofitting Non-Semantic Buttons
**Learning:** The application heavily relies on `div` elements with classes like `.catbtn` and `.medbtn` for interactivity, lacking native keyboard support. Retrofitting these with `role="button"` and `tabindex="0"` via a centralized JavaScript initializer proved more efficient and less invasive than rewriting thousands of lines of HTML.
**Action:** When facing large legacy codebases with widespread non-semantic interactive elements, use a centralized JS function to inject accessibility attributes and keyboard listeners on load, rather than refactoring the markup component by component.
