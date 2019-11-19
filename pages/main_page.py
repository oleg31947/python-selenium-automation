from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from pages.base_pages import Page

class MainPage(Page):
    SEARCH_INPUT = (By.ID, "twotabsearchtextbox")
    SEARCH_ICON = (By.CSS_SELECTOR, "input.nav-input[type='submit']")
    ORDER_LINK = (By.CSS_SELECTOR, "#nav-orders span.nav-line-2")
    HMB_MENU = (By.ID, "nav-hamburger-menu")
    SELECT_DEPARTMENT = (By.CSS_SELECTOR, "select.nav-search-dropdown")
    SELECTED_DEPARTMENT_SPAN = (By.CSS_SELECTOR, "#nav-search-dropdown-card span.nav-search-label")

    def search_for_keyword(self, text):
        self.input_text(text, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_ICON)

    def click_menu(self):
        self.click(*self.HMB_MENU)

    def select_department(self):
        select_department_element = self.find_element(*self.SELECT_DEPARTMENT)
        select = Select(select_department_element)
        select.select_by_value("search-alias=popular")

    def verify_select_department(self, expected_department):
        self.verify_text(expected_department, *self.SELECTED_DEPARTMENT_SPAN)



