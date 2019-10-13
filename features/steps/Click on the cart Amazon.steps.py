from behave import given, when, then
from selenium.webdriver.common.by import By

@given('Open Amazon page')
def open_amazon(context):
    context.driver.get("https://www.amazon.com/")

@when('Click on the cart icon')
def click_cart_icon(context):
    context.find_element(By.CSS_SELECTOR, "a#nav-cart" )
    context.send_keys('Cancel order')

@then('Verify Cart page open #Enter feature name here')
def verify_card_page_open(context):
    context.driver.find_element(By.By.CSS_SELECTOR, "div#sc-active-cart")