from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

PRIME_BUTTON_ICON = (By.CSS_SELECTOR, "a#nav-link-prime.nav-a.nav-a-2.nav-single-row-link")

@when('Click on Prime icon')
def search_prime_icon(context):
    context.driver.find_element(*PRIME_BUTTON_ICON).click()


