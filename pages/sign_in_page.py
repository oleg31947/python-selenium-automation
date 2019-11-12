from selenium.webdriver.common.by import By
from pages.base_pages import Page

class SignIn(Page):
    SING_IN_BTN = (By.XPATH, "//*[contains(text(),'Hello, Sign in')]")
    SING_IN_TEXT = (By.XPATH, "//h1[contains(text(),'Sign-In')]")

    def sign_in(self, expected_text):
        self.click(*self.SING_IN_BTN)
        self.verify_text(expected_text, *self.SING_IN_TEXT)