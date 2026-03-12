## 2024-05-23 - Event Delegation for Initialization Performance
**Learning:** Attaching `keydown` event listeners to over 1200 interactive elements in a loop during initialization caused measurable overhead.
**Action:** Replaced individual listeners with a single delegated event listener on `document` that checks `event.target.closest(selector)`. This reduces memory usage and speeds up `DOMContentLoaded` execution while preserving accessibility behavior (Enter/Space to click).

## 2026-03-07 - Recreating API Objects causes GC thrashing
**Learning:** Initializing browser API objects (like `IntersectionObserver`) inside high-frequency UI events (like `justify()`, which executes repeatedly on UI interactions) causes excessive Garbage Collection (GC) thrashing and spikes CPU overhead.
**Action:** Use a lazy-initialized singleton pattern. Instantiate the observer once, and use `.unobserve()` and `.observe()` to manage targets instead of disconnecting and recreating the object.

## 2026-03-08 - Synchronous Layout Thrashing via `getComputedStyle`
**Learning:** Using `getComputedStyle` within frequent UI click handlers forces the browser to flush the layout queue and recalculate styles synchronously, causing noticeable lag on lower-end devices.
**Action:** Avoid querying computed styles dynamically if the CSS variables can be statically mapped. I added a helper function to derive colors directly from static class names instead of forcing a layout calculation.

## 2026-03-09 - Repeated DOM Lookups in Click Handlers
**Learning:** Querying static DOM elements (like `.SOAPbox`, `.item-box`, `.SOAPbreak`) repeatedly inside high-frequency event listeners (like the delegated click handler for `.Aa` sliders) causes unnecessary DOM lookup overhead and potential layout thrashing.
**Action:** Cache static DOM elements outside of event listeners (or lazily initialize them) to reduce query overhead and improve interactivity performance.
