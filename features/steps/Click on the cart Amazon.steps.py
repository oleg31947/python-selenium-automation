from behave import given, when, then
from selenium.webdriver.common.by import By

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get("https://www.amazon.com/")

@when('Click on the card icon')
def search_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "a span#nav-cart-count"). click()

@then('Verifies that Your Shopping Cart is empty')
def verify_card_page_empty(context):
    context.driver.find_element(By.CSS_SELECTOR, "h1.sc-empty-cart-header")
    assert "Your Shopping Cart is empty"