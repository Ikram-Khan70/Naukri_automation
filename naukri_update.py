from playwright.sync_api import sync_playwright
import os

NAUKRI_EMAIL = os.getenv("NAUKRI_EMAIL")
NAUKRI_PASS = os.getenv("NAUKRI_PASS")
FULL_NAME = "Mohammed Ikram Khan"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    # Go to Naukri login page
    page.goto("https://www.naukri.com/mnjuser/login")

    # Login
    page.fill("input[name='username']", NAUKRI_EMAIL)
    page.fill("input[name='password']", NAUKRI_PASS)
    page.click("button[type='submit']")
    page.wait_for_timeout(5000)

    # Go to Profile Page
    page.goto("https://www.naukri.com/mnjuser/profile")  # Adjust URL if needed
    page.wait_for_timeout(3000)

    # Locate and update full name field (Example: placeholder logic)
    page.click("text='Edit'")  # Depends on actual selector
    page.fill("input[name='fullName']", FULL_NAME)
    page.click("button:has-text('Save')")  # Save button

    print("Profile updated successfully")
    browser.close()
