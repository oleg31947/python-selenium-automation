from selenium.webdriver.common.by import By
from pages.base_pages import Page

class MainPage(Page):
    SEARCH_INPUT = (By.ID, "twotabsearchtextbox")
    SEARCH_ICON = (By.CSS_SELECTOR, "input.nav-input[type='submit']")
    ORDER_LINK = (By.CSS_SELECTOR, "#nav-orders span.nav-line-2")
    HMB_MENU = (By.ID, "nav-hamburger-menu")

    def search_for_keyword(self, text):
        self.input_text(text, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_ICON)

    def click_menu(self):
        self.click(*self.HMB_MENU)




