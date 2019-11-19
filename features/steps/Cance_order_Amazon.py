from behave import given, when, then
from selenium.webdriver.common.by import By


@when('Input {serch_word} into search field.')
def open_cancel_order_page(context, search_word):
    context.driver.find_element(By.ID, "helpsearch")
    context.send_keys(search_word)

@when('Click on search icon.')
def click_search_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "span.a-button-inner").click()

@then('Verify Cancel Order page is opened.')
def verify_cancel_order_open(context):
    context.driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")





