from playwright.sync_api import sync_playwright, expect


def test_empty_courses_list():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

        registration_email_input = page.get_by_test_id('registration-form-email-input').locator('input')
        registration_email_input.fill('user.name@gmail.com')
        registration_username_input = page.get_by_test_id('registration-form-username-input').locator('input')
        registration_username_input.fill('username')
        registration_password_input = page.get_by_test_id('registration-form-password-input').locator('input')
        registration_password_input.fill('password')
        registration_button = page.get_by_test_id('registration-page-registration-button')
        registration_button.click()

        context.storage_state(path='browser_state.json')

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state='browser_state.json')
        page = context.new_page()
        page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        courses_page_header = page.get_by_test_id('courses-list-toolbar-title-text')
        expect(courses_page_header).to_have_text('Courses')
        courses_empty_block_icon = page.get_by_test_id('courses-list-empty-view-icon')
        expect(courses_empty_block_icon).to_be_enabled()
        courses_list_empty_title = page.get_by_test_id('courses-list-empty-view-title-text')
        expect(courses_list_empty_title).to_have_text('There is no results')
        courses_list_empty_description = page.get_by_test_id('courses-list-empty-view-description-text')
        expect(courses_list_empty_description).to_have_text(
            'Results from the load test pipeline will be displayed here')