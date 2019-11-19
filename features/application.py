from pages.main_page import MainPage
from pages.search_results_page import SearchResults
from pages.side_menu import SideMenu
from pages.product_page import Product
from pages.sign_in_page import SignIn


class Application:

    def __init__(self, driver):
        self.driver = driver
        self.product_page = Product(self.driver)
        self.main_page = MainPage(self.driver)
        self.search_results_page = SearchResults(self.driver)
        self.sign_in_page = SignIn(self.driver)
        self.side_menu = SideMenu(self.driver)



