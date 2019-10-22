from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

CARD_ITEM_COUNT = (By.ID, 'nav-cart-count')

@when('Click Add to card button')
def click_add_cart_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "input#add-to-cart-button.a-button-input").click()

@then('Verify cart has {expected_item_count} item.')
def verify_item_count(context, expected_item_count):
    sleep(3)
    actual_items = context.driver.find_element(*CARD_ITEM_COUNT).text
    assert actual_items == expected_item_count, f'Expected {expected_item_count}, but got {actual_items}'
