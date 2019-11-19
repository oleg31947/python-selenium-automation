from selenium.webdriver.common.by import By
from behave import given, when, then


@when('Hover over SALES & DEALS')
def hover_add_sales_deals(context):
    context.app.product_page.hover_add_sales_deals()

@then('Verify fashion tooltip is shown')
def verify_fashion_tooltip(context):
    context.app.product_page.verify_fashion_tooltip()
