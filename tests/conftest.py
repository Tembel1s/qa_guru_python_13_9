import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def setup_browser(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver
    browser.config.base_url = "https://demoqa.com"

    yield browser
    browser.quit()

# @pytest.fixture(scope="function", autouse=True)
# def browser_management():
#     browser.config.base_url = "https://demoqa.com"
#     browser.config.window_width = 1920
#     browser.config.window_height = 1080
#     driver_options = webdriver.ChromeOptions()
#     driver_options.page_load_strategy = "eager"
#     browser.config.driver_options = driver_options
#     yield
#     browser.quit()