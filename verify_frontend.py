from playwright.sync_api import sync_playwright
import sys

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://localhost:8000")

        # Click Category A
        page.wait_for_selector("#btnA")
        page.click("#btnA")
        page.wait_for_timeout(500)

        # Click Subcategory A-1
        page.wait_for_selector("#btnA1")
        page.click("#btnA1")
        page.wait_for_timeout(500)

        page.screenshot(path="verification.png")
        browser.close()

if __name__ == "__main__":
    run()
