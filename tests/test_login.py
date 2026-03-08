from pages.login_page import LoginPage
from pages.nav_bar_locators import NavBarLocators
from core.config import Config

def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.login(Config.TEST_EMAIL, Config.TEST_PASSWORD)
    assert "automationexercise.com" in page.url
    assert page.locator(NavBarLocators.LOGOUT_LINK).is_visible()
