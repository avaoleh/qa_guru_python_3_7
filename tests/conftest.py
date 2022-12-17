import pytest
from selene.support.shared import browser
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import allure

@pytest.fixture()
def config_webdriver():
    with allure.step('Инициализируем драйвер браузераа'):
        browser.config.driver = webdriver.Chrome(ChromeDriverManager().install())
        return browser.config.driver

@pytest.fixture()
def config_browser_size():
    with allure.step('Конфигурация размера окна браузера'):
        browser.config.window_height = 1920
        browser.config.window_width = 1620


@pytest.fixture()
def open_browser(config_webdriver, config_browser_size):
    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com')