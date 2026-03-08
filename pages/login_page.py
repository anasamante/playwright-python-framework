from core.base_page import BasePage
from pages.login_locators import LoginLocators
from pages.base_locators import BaseLocators
from core.config import Config


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def login(self, email, password):
        self.consent_overlay(BaseLocators.CONSENT_BUTTON)
        self.navigate(Config.BASE_URL + "/login")
        self.fill(LoginLocators.LOGIN_EMAIL, email)
        self.fill(LoginLocators.LOGIN_PASSWORD, password)
        self.click(LoginLocators.LOGIN_BUTTON)