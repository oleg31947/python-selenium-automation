from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from time import sleep

SEARCH_INPUT = (By.NAME, 'q')
RESULTS_FOUND_MESSAGE = (By.XPATH, "//div[contains(@class,'commercial-unit-desktop-top')]")
CARD_BTN = (By.CSS_SELECTOR, "input#add-to-cart-button.a-button-input")
ORDER_LINK = (By.CSS_SELECTOR, "#nav-orders span.nav-line-2")
HAMBURGER_MENU = (By.ID, "nav-hamburger-menu")
SIGN_IN_TEX = (By.CSS_SELECTOR, "h1.a-spacing-small")
RESULTS = (By.XPATH, "//div[@class='g']")
CARD_ITEM_COUNT = (By.ID, 'nav-cart-count')
SEARCH_SUBMIT = (By.NAME, 'btnK')
AMAZON_PRIME_MENU_ITEM_RESULTS = (By.CSS_SELECTOR, "div.benefit-box")

@given('Open Amazon Help')
def open_amazon(context):
    context.driver.get("https://www.amazon.com/gp/help/customer/display.html")


@given('Open {specific} Amazon page')
def open_specific_Amazon_page(context, specific):
    context.driver.get(f'https://www.amazon.com/gp/product/{specific}/')


@given('Open Google page')
def open_google(context):
    context.driver.get('https://www.google.com/')


@when('Select {department} department')
def select_department(context, department):
    context.app.main_page.select_department()


@when('Input {search_word} into search field')
def input_search(context, search_word):
    search = context.driver.find_element(*SEARCH_INPUT)
    search.clear()
    search.send_keys(search_word)
    sleep(4)


@when('Click Amazon {link}')
def click_amazon_order_link(context, link):
    context.app.main_page.click(*ORDER_LINK)


@when('Click on search icon')
def click_search_icon(context):
    context.driver.find_element(*SEARCH_SUBMIT).click()
    sleep(1)


@when('Click Add to card button')
def click_add_cart_button(context):
    context.driver.find_element(*CARD_BTN).click()


@when('Click on hamburger menu')
def click_on_hamburger_menu(context):
    # context.app.main_page.click(*HAMBURGER_MENU)
    context.app.main_page.click_menu()


@when('Click on Amazon {Music} menu item')
def click_on_Amazon_Music(context, Music):
    context.app.side_menu.click_music()


@then('{department} department is selected')
def verify_select_department(context, department):
    context.app.main_page.verify_select_department(department)


@then('Product results for {search_word} are shown')
def verify_found_results_text(context, search_word):
    results_msg = context.driver.find_element(*RESULTS_FOUND_MESSAGE).text
    assert search_word in results_msg, "Expected word '{}' in message, but got '{}'".format(search_word, results_msg)


@then('Verify {expected_text} page is opened')
def verify_text_sign_in(context, expected_text):
    context.app.main_page.verify_text(expected_text, *SIGN_IN_TEX)


@then('{expected_item_count} menu items are present')
def verify_item_count(context, expected_item_count):
    expected_item_count = int(expected_item_count)
    context.app.side_menu.verify_amount_of_items(expected_item_count)


@then('Verify cart has {expected_item_count} item.')
def verify_item_count(context, expected_item_count):
    sleep(3)
    actual_items = context.driver.find_element(*CARD_ITEM_COUNT).text
    assert actual_items == expected_item_count, f'Expected {expected_item_count}, but got {actual_items}'


@then('First result contains {search_word}')
def verify_first_result(context, search_word):
    first_result = context.driver.find_element(*RESULTS).text
    print('\n{}'.format(first_result))
    assert search_word in first_result, "Expected word '{}' in message, but got '{}'".format(search_word, first_result)


@then('{expected_item_count} boxes are present')
def verify_amount_of_boxes(context, expected_item_count):
    context.driver.find_elements(*AMAZON_PRIME_MENU_ITEM_RESULTS)
    sleep(3)
    actual_items = (len(context.driver.find_elements(*AMAZON_PRIME_MENU_ITEM_RESULTS)))
    assert int(expected_item_count) == actual_items, f'Expected {expected_item_count}, but got {actual_items}'
