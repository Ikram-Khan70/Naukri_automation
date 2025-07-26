from playwright.sync_api import sync_playwright
import os

NAUKRI_EMAIL = os.getenv("NAUKRI_EMAIL")
NAUKRI_PASS = os.getenv("NAUKRI_PASS")
FULL_NAME = "Mohammed Ikram Khan"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    # 1. Go to login page
    page.goto("https://www.naukri.com/mnjuser/login", timeout=60000)
    page.wait_for_timeout(5000)

    # 2. Fill login form
    page.get_by_placeholder("Email ID / Username").fill(NAUKRI_EMAIL)
    page.get_by_placeholder("Password").fill(NAUKRI_PASS)
    page.get_by_role("button", name="Login").click()
    page.wait_for_timeout(8000)
    page.screenshot(path="after_login.png")

    # 3. Go to Profile
    page.goto("https://www.naukri.com/mnjuser/profile", timeout=60000)
    page.wait_for_timeout(8000)
    page.screenshot(path="profile_loaded.png")

    # 4. Click the pencil/edit icon for Full Name
    page.locator("div.edit-icon").first.click()  # this may need adjustment
    page.wait_for_timeout(2000)

    # 5. Edit the Full Name field
    name_field = page.get_by_placeholder("Full Name")
    name_field.fill("")  # Clear the field
    name_field.type(FULL_NAME)
    page.screenshot(path="edited_name.png")

    # 6. Click Save/Update button (adjust the selector if needed)
    page.get_by_role("button", name="Save").click()
    page.wait_for_timeout(3000)
    page.screenshot(path="name_saved.png")

    print("✅ Full Name updated successfully.")
    browser.close()
