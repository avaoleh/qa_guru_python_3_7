import allure
from selene.support import by
from selene.support.conditions import be
from selene.support.shared import browser
from selene.support.shared.jquery_style import s


def test_dynamic_steps(open_browser):
    # with allure.step("Открываем главную страницу"):
    #     browser.open("https://github.com")

    with allure.step("Ищем репозитория"):
        s(".header-search-input").click()
        s(".header-search-input").send_keys("avaoleh/qa_guru_python_3_7")
        s(".header-search-input").submit()

    with allure.step("Переходим по ссылке репозитория"):
        s(by.link_text("avaoleh/qa_guru_python_3_7")).click()

    with allure.step("Открываем таб Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issue с номером 1"):
        s(by.partial_text("#1")).should(be.visible)


def test_decorator_steps(open_browser):
    #open_main_page()
    search_for_repository("avaoleh/qa_guru_python_3_7")
    go_to_repository("avaoleh/qa_guru_python_3_7")
    open_issue_tab()
    should_see_issue_with_number("#1")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("https://github.com")


@allure.step("Ищем репозитория {repo}")
def search_for_repository(repo):
    s(".header-search-input").click()
    s(".header-search-input").send_keys(repo)
    s(".header-search-input").submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем наличие Issue с номером {number}")
def should_see_issue_with_number(number):
    s(by.partial_text(number)).click()
