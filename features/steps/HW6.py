from time import sleep
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


NEW_PAGE = (By. XPATH, "//a[contains(@aria-label, 'deals under $25')]")
TODAYS_DEALS_HEADER = (By. XPATH, "//h1[contains(text(),'Shop all deals')]")
SEARCH_RESULT = (By. XPATH, "//a[@id='103 f3bca6e2-announce']")
ADD_TO_CART = (By.CSS_SELECTOR, "input#add-to-cart-button.a-button-input")

BOOKS_LINK = (By.CSS_SELECTOR, "a[href*='best-sellers-books-Amazon/zgbs/books/ref=zg_bs_books']")
BOOKS = (By.CSS_SELECTOR, "h1.a-size-large.a-spacing-medium.zg-margin-left-15.a-text-bold")


@when("Store original window")
def store_original_window(context):
    context.original_window = context.driver.current_window_handle
    context.old_windows = context.driver.window_handles
    print('\noriginal_window\n', context.original_window)
    print('\nold_windows\n', context.old_windows)

@when("Click to open {new_page}")
def click_to_open_page(context, new_page):
    context.driver.find_element(*NEW_PAGE).click()

@when("Switch to the new opened window")
def switch_to_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    current_windows = context.driver.window_handles
    print('\ncurrent_windows\n', current_windows)

    new_window = current_windows[1]
    print('\nnew_window\n', new_window)
    context.driver.switch_to_window(new_window)
    sleep(3)

@then ("{expected_header} are shown.")
def header_is_correct(context, expected_header):
    actual_header = context.driver.find_element(*TODAYS_DEALS_HEADER).text
    assert actual_header == expected_header, f'Expected {expected_header}, but got {actual_header}'

@when('Put {product} into a cart')
def click_add_cart_button(context, product):
    context.driver.find_element(*SEARCH_RESULT).click()
    context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART))
    context.driver.find_element(*ADD_TO_CART).click()


@when("Close new window, switch back to original")
def close_and_switch_window(context):
    sleep(3)
    context.driver.close()
    sleep(3)
    context.driver.switch_to_window(context.original_window)
    print('\noriginal_window\n', context.original_window)

@when('Refresh the page')
def refresh_page(context):
    context.driver.refresh()

