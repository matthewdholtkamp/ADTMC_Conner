from playwright.sync_api import sync_playwright

def verify_aria_expanded():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("http://localhost:8080/index.html")

        # Use force=True to bypass potential overlay issues during navigation
        print("Clicking Category A...")
        page.locator("#btnA").click(force=True)
        page.wait_for_timeout(500)

        print("Clicking Subcategory A-1...")
        page.locator("#btnA1").click(force=True)
        page.wait_for_timeout(500)

        # Target the first .contbox-top inside the visible content
        # .info-container should now be active
        header = page.locator(".info-container.active .contbox-top").first

        # Ensure header is actually visible before interacting
        if not header.is_visible():
            print("Header not visible, forcing visibility for test...")
            page.evaluate("document.querySelector('.info-container').classList.add('active')")
            header = page.locator(".contbox-top").first

        print("Checking initial state...")
        # Check if attribute exists
        aria_expanded = header.get_attribute("aria-expanded")
        print(f"Initial aria-expanded: {aria_expanded}")

        # Attempt to click header to toggle
        print("Clicking header...")
        header.click(force=True)
        page.wait_for_timeout(500)

        aria_expanded_after = header.get_attribute("aria-expanded")
        print(f"After 1st click aria-expanded: {aria_expanded_after}")

        # Attempt click again
        print("Clicking header again...")
        header.click(force=True)
        page.wait_for_timeout(500)

        aria_expanded_final = header.get_attribute("aria-expanded")
        print(f"After 2nd click aria-expanded: {aria_expanded_final}")

        browser.close()

if __name__ == "__main__":
    verify_aria_expanded()
