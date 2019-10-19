from behave import given, when, then
from selenium.webdriver.common.by import By

SEARCH_INPUT = (By.ID, "twotabsearchtextbox")
SEARCH_ICON = (By. CSS_SELECTOR, "input.nav-input[type='submit']")
PRODUCT_RESULTS = (By. XPATH, "//li[@role='listitem']//a[@class='a-size-base a-link-normal s-no-hover a-text-normal']")

@when('Search for {product}')
def search_product(context, product):
    search_field = context.driver.find_element(*SEARCH_INPUT)
    search_field.clear()
    search_field.send_keys(product)
    context.driver.find_element(*SEARCH_ICON).click()
@when('Open the first product search result')
def click_first_result(context):
    context.driver.find_elemet(*PRODUCT_RESULTS).click()



