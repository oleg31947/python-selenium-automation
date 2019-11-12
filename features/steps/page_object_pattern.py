from selenium.webdriver.common.by import By
from time import sleep
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from pages.base_pages import Page

ORDER_LINK = (By. CSS_SELECTOR, "#nav-orders span.nav-line-2")
SIGN_IN_TEX = (By.CSS_SELECTOR, "h1.a-spacing-small")
HAMBURGER_MENU = (By.ID, "nav-hamburger-menu")

@when('Click Amazon {link}')
def click_amazon_order_link(context, link):
    context.app.main_page.click(*ORDER_LINK)

@then('Verify {expected_text} page is opened')
def verify_text_sign_in(context, expected_text):
    context.app.main_page.verify_text(expected_text, *SIGN_IN_TEX)

@when('Click on hamburger menu')
def click_on_hamburger_menu(context):
    #context.app.main_page.click(*HAMBURGER_MENU)
    context.app.main_page.click_menu()

@when('Click on Amazon Music menu item')
def click_on_Amazon_Music(context):
    context.app.side_menu.click_music()

@then('{expected_item_count} menu items are present')
def verify_item_count(context, expected_item_count):
    expected_item_count = int(expected_item_count)
    context.app.side_menu.verify_amount_of_items(expected_item_count)



