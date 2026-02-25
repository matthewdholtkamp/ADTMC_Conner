# Bolt's Journal

## 2024-05-22 - Optimize Search Rendering
**Learning:** Appending elements to the DOM in a loop causes multiple reflows/repaints, which is a performance bottleneck, especially for search results that update frequently.
**Action:** Use `DocumentFragment` to batch DOM insertions. This allows building the entire subtree off-DOM and appending it in a single operation, triggering only one reflow. This was implemented in `testing.js` for the global search results.
