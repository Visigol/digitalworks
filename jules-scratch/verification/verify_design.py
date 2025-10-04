import os
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        current_dir = os.getcwd()

        # Navigate to index.html and take a screenshot
        page.goto(f"file://{current_dir}/index.html")
        page.screenshot(path="jules-scratch/verification/index.png")

        # Navigate to career.html and take a screenshot
        page.goto(f"file://{current_dir}/career.html")
        page.screenshot(path="jules-scratch/verification/career.png")

        # Navigate to digitalworks.html and take a screenshot
        page.goto(f"file://{current_dir}/digitalworks.html")
        page.screenshot(path="jules-scratch/verification/digitalworks.png")

        # Navigate to contact.html and take a screenshot
        page.goto(f"file://{current_dir}/contact.html")
        page.screenshot(path="jules-scratch/verification/contact.png")

        browser.close()

if __name__ == "__main__":
    run()