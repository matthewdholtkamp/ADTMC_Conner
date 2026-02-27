
from playwright.sync_api import sync_playwright

def verify_aria_expanded():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto('http://localhost:8080/index.html')

        # Navigate to a section (e.g., A -> A-1)
        page.click('#btnA')
        page.click('#btnA1')

        # Locate the header of a collapsible section (e.g., the partial DDX one)
        # In index.html, the structure is:
        # <div class="sub-page-pre">
        #   <div class="contbox">
        #     <div class="contbox-top">...</div>

        # We need to find one that is visible.
        # After clicking A-1, the sub-page opens.
        # Let's target the first visible .contbox-top

        header = page.locator('.contbox-top').first

        # 1. Check initial state
        initial_state = header.get_attribute('aria-expanded')
        print(f"Initial aria-expanded: {initial_state}")

        # Take screenshot of initial state
        page.screenshot(path="verification/aria_initial.png")

        # 2. Click to toggle
        header.click()

        # 3. Check state after click
        after_click_state = header.get_attribute('aria-expanded')
        print(f"After 1st click aria-expanded: {after_click_state}")

        # Take screenshot of expanded state
        page.screenshot(path="verification/aria_expanded.png")

        # 4. Click again to toggle back
        header.click()

        # 5. Check state after second click
        final_state = header.get_attribute('aria-expanded')
        print(f"After 2nd click aria-expanded: {final_state}")

        browser.close()

if __name__ == "__main__":
    verify_aria_expanded()
