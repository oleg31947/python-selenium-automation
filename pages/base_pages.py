from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page:
    def __init__(self, driver):
       self.driver = driver
       self.base_url = 'https://www.amazon.com/'
       self.waite = WebDriverWait(self.driver, 15)

    def click(self, *locator):
        self.driver.find_element(*locator).click()


    def input_text(self, text, *locator):
        e = self.driver.find_element(*locator)
        e.clear()
        e.send_keys(text)

    def open_page(self, url=' '):
        self.driver.get(self.base_url + url)

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        print(actual_text)
        print(expected_text)
        assert expected_text == actual_text, f'Expected text {expected_text}, but got (actual_text)'

    def wait_for_element_click(self, *locator):
        e = self.driver.wait.until(EC.element_to_be_clickable(locator))
        e.click()


