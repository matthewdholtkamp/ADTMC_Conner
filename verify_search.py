from playwright.sync_api import sync_playwright

def verify_search_accessibility():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8080/index.html")

        # 1. Verify initial state
        search_input = page.get_by_role("combobox", name="Search content")
        assert search_input.is_visible()
        assert search_input.get_attribute("aria-expanded") == "false"
        assert search_input.get_attribute("aria-controls") == "searchResults"

        search_results = page.get_by_role("listbox")
        assert search_results.is_hidden() # Should be hidden initially

        print("Initial state verified.")

        # 2. Type "A" (should not trigger search due to length < 2)
        search_input.type("A")
        page.wait_for_timeout(500) # Wait for debounce
        assert search_input.get_attribute("aria-expanded") == "false"
        assert search_results.is_hidden()
        print("Length check verified.")

        # 3. Type "Ad" (should trigger search)
        search_input.type("d")
        page.wait_for_timeout(500) # Wait for debounce

        # Verify expanded
        assert search_input.get_attribute("aria-expanded") == "true"
        assert search_results.is_visible()

        # Verify results
        # Should have items with role="option"
        options = search_results.locator('[role="option"]')
        count = options.count()
        print(f"Found {count} options.")
        assert count > 0

        # Verify NO aria-live (should be removed when results are found)
        assert search_results.get_attribute("aria-live") is None

        page.screenshot(path="verification_results.png")
        print("Results state verified.")

        # 4. Type "Zzzzz" (No results)
        search_input.fill("Zzzzz")
        page.wait_for_timeout(500)

        assert search_input.get_attribute("aria-expanded") == "true"
        assert search_results.is_visible()

        # Verify aria-live is present
        assert search_results.get_attribute("aria-live") == "polite"
        assert "No results found" in search_results.text_content()

        page.screenshot(path="verification_no_results.png")
        print("No results state verified.")

        # 5. Clear (or click outside)
        page.mouse.click(0, 0)
        assert search_input.get_attribute("aria-expanded") == "false"
        assert search_results.is_hidden()
        print("Closing verified.")

        browser.close()

if __name__ == "__main__":
    verify_search_accessibility()
