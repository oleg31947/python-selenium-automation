from selenium.webdriver.common.by import By
from pages.base_pages import Page
from time import sleep

class SideMenu(Page):
    AMAZON_MUSIC_ITEM = (By.XPATH, "//ul[contains(@class,'hmenu-visible')]//div[contains(text(),'Amazon Music')]")
    AMAZON_MUSIC_MENU_ITEM_RESULTS = (By.CSS_SELECTOR, "ul.hmenu-visible a:not(.hmenu-back-button)")

    def click_music(self):
        self.wait_for_element_click(*self.AMAZON_MUSIC_ITEM)
        self.driver.find_element(*self.AMAZON_MUSIC_ITEM)
        sleep(2)

    def verify_amount_of_items(self, expected_item_count:int):
        actual_item_count = len(self.driver.find_elements(*self.AMAZON_MUSIC_MENU_ITEM_RESULTS))
        self.wait_for_element_click(*self.AMAZON_MUSIC_MENU_ITEM_RESULTS)
        print(type(actual_item_count))
        print(actual_item_count)
        assert actual_item_count == expected_item_count, f'Expected text {expected_item_count}, but got (actual_item_count)'

