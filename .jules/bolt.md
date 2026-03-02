## 2024-05-23 - Event Delegation for Initialization Performance
**Learning:** Attaching `keydown` event listeners to over 1200 interactive elements in a loop during initialization caused measurable overhead.
**Action:** Replaced individual listeners with a single delegated event listener on `document` that checks `event.target.closest(selector)`. This reduces memory usage and speeds up `DOMContentLoaded` execution while preserving accessibility behavior (Enter/Space to click).
