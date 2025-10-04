import os
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        current_dir = os.getcwd()

        # Verify career page
        page.goto(f"file://{current_dir}/career.html")
        # Click the first timeline item to expand it
        page.click('.timeline-item-header')
        page.wait_for_timeout(1000) # Wait for animation
        page.screenshot(path="jules-scratch/verification/career_expanded.png", full_page=True)

        # Verify contact page
        page.goto(f"file://{current_dir}/contact.html")
        page.screenshot(path="jules-scratch/verification/contact_updated.png", full_page=True)

        browser.close()

if __name__ == "__main__":
    run()