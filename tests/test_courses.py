import pytest
from playwright.sync_api import expect, Page
from fixtures.pages import create_course_page, courses_list_page
from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage


@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state: Page):
    page = chromium_page_with_state
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')
    courses_page_header = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(courses_page_header).to_have_text('Courses')
    courses_empty_block_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(courses_empty_block_icon).to_be_enabled()
    courses_list_empty_title = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(courses_list_empty_title).to_have_text('There is no results')
    courses_list_empty_description = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(courses_list_empty_description).to_have_text('Results from the load test pipeline will be displayed here')


def test_create_course(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
    create_course_page.vizit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view()
    create_course_page.check_visible_create_course_form(
        title='',
        description='',
        estimated_time='',
        max_score='0',
        min_score='0'
    )
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()
    create_course_page.upload_preview_image('./testdata/files/image.png')
    create_course_page.check_visible_image_upload_view()
    create_course_page.fill_create_course_form(
        title='Playwright',
        estimated_time='2 weeks',
        description='Playwright',
        max_score='100',
        min_score='10'
    )
    create_course_page.click_create_course_button()
    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_course_card(
        index=0,
        title='Playwright',
        estimated_time='2 weeks',
        max_score='100',
        min_score='10'
    )
