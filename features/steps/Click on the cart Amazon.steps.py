from behave import given, when, then
from selenium.webdriver.common.by import By

CART_ICON = (By.CSS_SELECTOR, "a#nav-cart.nav-a.nav-a-2")
CART_IS_EMTY = (By.CSS_SELECTOR, "h1.sc-empty-cart-header")

@given('Open Amazon page')
def open_amazon(context):
    #context.driver.get("https://www.amazon.com/")
    context.app.main_page.open_page()

@when('Click on cart icon')
def search_cart_icon(context):
    context.app.main_page.click(*CART_ICON)
    #context.driver.find_element(*CART_ICON).click()

@then('Verify {expected_text} text present')
def verify_card_page_empty(context, expected_text):
    #actual_text = context.driver.find_element(*CART_IS_EMTY).text
    #assert actual_text == expected_text
    context.app.main_page.verify_text(expected_text, *CART_IS_EMTY)

