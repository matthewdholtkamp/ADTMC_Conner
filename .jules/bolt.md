## 2024-05-23 - Event Delegation for Initialization Performance
**Learning:** Attaching `keydown` event listeners to over 1200 interactive elements in a loop during initialization caused measurable overhead.
**Action:** Replaced individual listeners with a single delegated event listener on `document` that checks `event.target.closest(selector)`. This reduces memory usage and speeds up `DOMContentLoaded` execution while preserving accessibility behavior (Enter/Space to click).

## 2026-03-07 - Recreating API Objects causes GC thrashing
**Learning:** Initializing browser API objects (like `IntersectionObserver`) inside high-frequency UI events (like `justify()`, which executes repeatedly on UI interactions) causes excessive Garbage Collection (GC) thrashing and spikes CPU overhead.
**Action:** Use a lazy-initialized singleton pattern. Instantiate the observer once, and use `.unobserve()` and `.observe()` to manage targets instead of disconnecting and recreating the object.
