# def browser():
#
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture
def browser(playwright_instance, config):
    headless_mode = config['headless']
    browser_mode = config['browser_name']
    # env_mode = config['env']
    browser = getattr(playwright_instance, browser_mode).launch(headless=headless_mode)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()
    yield context
    context.close()


@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    yield page
    page.close()


def pytest_addoption(parser):
    # parser.addoption("--env", action="store", default="dev", help="Set environment: dev/stage/prod")
    parser.addoption("--browser-name", action="store", default="chromium", help="Browser: chromium/firefox/webkit")
    parser.addoption("--headless", action="store_true", help="Run browser in headless mode")


@pytest.fixture(scope="session")
def config(request):
    return {
        # "env": request.config.getoption("--env"),
        "browser_name": request.config.getoption("--browser-name"),
        "headless": request.config.getoption("--headless")
    }
