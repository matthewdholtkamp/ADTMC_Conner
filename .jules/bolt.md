## 2024-05-23 - Layout Thrashing in Initialization Loops
**Learning:** Using `innerText` inside a loop over ~150 DOM elements during `DOMContentLoaded` caused significant layout thrashing (forced reflows), blocking the main thread for ~70ms. This is because `innerText` requires the browser to calculate the layout to determine visibility.
**Action:** Prefer `textContent` over `innerText` when reading text from DOM elements in loops, especially during initialization, unless visibility awareness is explicitly required. Switching to `textContent` reduced the operation time to ~1.7ms (42x improvement).

## 2024-05-24 - DocumentFragment for Appending Lists
**Learning:** During category navigation (A-M to A-1, etc.), appending elements repeatedly inside a loop to an unattached `ul` was inefficient. While not causing layout thrashing (since the `ul` wasn't attached to the DOM yet), the code unnecessarily reassigned `innerHTML` multiple times inside the loop and created an implicit global variable (`i`).
**Action:** Use a `DocumentFragment` to batch the addition of child elements (`li`) to their parent (`ul`), ensuring performance best practices and eliminating unnecessary innerHTML assignments. Always use `let` or `const` for loop counters to prevent leaking them into the global scope.
