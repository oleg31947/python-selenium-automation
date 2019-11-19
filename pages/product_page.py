from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_pages import Page
from time import sleep

class Product(Page):
    SALES_DEALS_BTN = (By.XPATH, "//a[@class='nav-a nav-hasArrow']/*[contains(text(),'SALES & DEALS')]")
    FASHION_TOOLTIP = (By.XPATH, "//a[@class='mm-merch-panel']/*[contains(@src,'flyout__fall3_women._CB448971046_.jpg')]")


    def open_product(self, product_id):
        self.open_page(f'dp/{product_id}')

    def hover_add_sales_deals(self):
        sales_deals = self.find_element(*self.SALES_DEALS_BTN)
        self.action.move_to_element(sales_deals).perform()
        sleep(2)

    def verify_fashion_tooltip(self):
        self.wait_for_element_appear(*self.FASHION_TOOLTIP)


