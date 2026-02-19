## 2026-02-19 - Accessibility Retrofit for Multi-State Icons
**Learning:** When retrofitting accessibility onto a legacy codebase where a `div` acts as a multi-state button (e.g., transitioning between Menu/Back/Close icons), static `aria-label`s are insufficient. The label must be updated dynamically in the JavaScript logic that controls the visual state change to ensure screen readers announce the current function, not just the initial one.
**Action:** Always pair visual state transition functions (like `showMenu`, `showArrow`) with a corresponding `setAttribute('aria-label', ...)` call.
