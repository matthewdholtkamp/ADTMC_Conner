## 2024-05-23 - Event Delegation for Initialization Performance
**Learning:** Attaching `keydown` event listeners to over 1200 interactive elements in a loop during initialization caused measurable overhead.
**Action:** Replaced individual listeners with a single delegated event listener on `document` that checks `event.target.closest(selector)`. This reduces memory usage and speeds up `DOMContentLoaded` execution while preserving accessibility behavior (Enter/Space to click).

## 2024-05-24 - Event Delegation for Click Events
**Learning:** The application initialized click event listeners on over 460 `.Aa` elements individually using `querySelectorAll` and a `forEach` loop. This codebase-specific pattern caused unnecessary memory overhead and layout thrashing during initialization. Event delegation on the document level is the most performant approach in this codebase, extending the existing learning from keydown events.
**Action:** Replaced the loop with a single `document.addEventListener('click', ...)` that checks for `event.target.closest('.Aa')`. Always use event delegation when binding to numerous interactive elements in this app.
