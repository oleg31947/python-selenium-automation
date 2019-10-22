from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

PRIME_BUTTON_ICON = (By.CSS_SELECTOR, "a#nav-link-prime.nav-a.nav-a-2.nav-single-row-link")
AMAZON_PRIME_MENU_ITEM_RESULTS = (By.CSS_SELECTOR, "div.a-section .a-padding-base")

@when('Click on Prime icon')
def search_prime_icon(context):
    context.driver.find_element(*PRIME_BUTTON_ICON).click()

@then('{expected_item_count} boxes are present')
def verify_amount_of_boxes(context, expected_item_count):
    context.driver.find_elements(*AMAZON_PRIME_MENU_ITEM_RESULTS)
    sleep(3)

    actual_items = len(context.driver.find_elements(*AMAZON_PRIME_MENU_ITEM_RESULTS))*2
    assert actual_items == int(expected_item_count), f'Expected {expected_item_count}, but got {actual_items}'
