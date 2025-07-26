# naukri_update.py
import os
from playwright.sync_api import sync_playwright

NAUKRI_EMAIL = os.environ["NAUKRI_EMAIL"]
NAUKRI_PASS = os.environ["NAUKRI_PASS"]

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # Step 1: Go to login page
    page.goto("https://www.naukri.com/mnjuser/login", timeout=60000)
    page.screenshot(path="login_page.png")

    # Step 2: Login
    page.wait_for_selector("input[type='text']")
    page.locator("input[type='text']").fill(NAUKRI_EMAIL)
    page.locator("input[type='password']").fill(NAUKRI_PASS)
    page.get_by_role("button", name="Login").click()

    # Step 3: Wait for login & navigate to profile
    page.wait_for_timeout(8000)
    page.goto("https://www.naukri.com/mnjuser/profile", timeout=60000)
    page.wait_for_timeout(5000)
    page.screenshot(path="after_login.png")

    # Step 4: Click edit name button
    page.click("span:has-text('Edit')")  # may need tuning
    page.wait_for_selector("input[placeholder='Full Name']")
    page.fill("input[placeholder='Full Name']", "Mohammed Ikram Khan")
    page.get_by_role("button", name="Save").click()
    page.wait_for_timeout(4000)

    page.screenshot(path="profile_updated.png")
    browser.close()
