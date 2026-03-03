# global test setup
import pytest
from playwright.sync_api import sync_playwright
from core.config import Config


@pytest.fixture(scope="session")   # global setup for the entire test session
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        yield browser
        browser.close()


@pytest.fixture(scope="function")   # setup for each individual test function
def page(browser):
    page = browser.new_page()
    page.goto(Config.BASE_URL)
    yield page
    page.close()