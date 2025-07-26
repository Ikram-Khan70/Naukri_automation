from playwright.sync_api import sync_playwright
import os

# Environment variables from GitHub Secrets
NAUKRI_EMAIL = os.getenv("NAUKRI_EMAIL")
NAUKRI_PASS = os.getenv("NAUKRI_PASS")
FULL_NAME = "Mohammed Ikram Khan"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    # Go to login page
    page.goto("https://www.naukri.com/mnjuser/login")

    # Wait and fill login credentials
    page.wait_for_selector("input[name='username']", timeout=15000)
    page.fill("input[name='username']", NAUKRI_EMAIL)

    page.wait_for_selector("input[name='password']", timeout=10000)
    page.fill("input[name='password']", NAUKRI_PASS)

    # Click login
    page.click("button[type='submit']")
    page.wait_for_timeout(5000)  # Let the page load

    # Save screenshot after login attempt
    page.screenshot(path="after_login.png")

    print("Login attempt finished.")
    browser.close()
