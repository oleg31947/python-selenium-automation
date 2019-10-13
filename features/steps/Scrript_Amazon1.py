from behave import given, when, then
from selenium.webdriver.common.by import By

@given('Open Amazon URL')
def open_amazon(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html")

@when('Open Amazon Cancel Order')
def open_cancel_order_page(context):
    context.find_element(By.XPATH, "//input[@type='search'and @id='helpsearch']")
    context.send_keys('Cancel order')

@then('Verify Cancel Order page is opened')
def verify_cancel_order_open(context):
    context.driver.find_element(By.By.XPATH, "//input[@class='a-button-input']")





