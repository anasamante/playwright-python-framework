from pages.login_page import LoginPage
from pages.nav_bar_locators import NavBarLocators
from pages.login_locators import LoginLocators
from core.config import Config

def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.login(Config.TEST_EMAIL, Config.TEST_PASSWORD)
    assert "automationexercise.com" in page.url
    assert page.locator(NavBarLocators.LOGOUT_LINK).is_visible()


def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.login("invalid@email.com", "invalidpassword")
    assert "Your email or password is incorrect!" in login_page.get_text(LoginLocators.LOGIN_ERROR)
