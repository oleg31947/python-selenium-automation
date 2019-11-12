from pages.main_page import MainPage
from pages.search_results_page import SearchResults
from pages.side_menu import SideMenu
from pages.sign_in_page import SignIn


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.search_results_page = SearchResults(self.driver)
        self.sign_in_page = SignIn(self.driver)
        self.side_menu = SideMenu(self.driver)



