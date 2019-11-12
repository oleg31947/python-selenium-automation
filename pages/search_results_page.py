from selenium.webdriver.common.by import By
from pages.base_pages import Page

class SearchResults(Page):
    TODAYS_DEALS_HEADER = (By.XPATH, "//h1[contains(text(),'Shop all deals')]")

    def verify_result_shown(self, expected_text):
        self.verify_text(expected_text, *self.TODAYS_DEALS_HEADER)