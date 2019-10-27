
from behave import given, when, then
from selenium.webdriver.common.by import By

COLOR_OPTIONS = (By.CSS_SELECTOR, "div#variation_color_name li")
SELECTED_COLOR = (By.CSS_SELECTOR, "div#variation_color_name .selection")

@given('Open {specific} Amazon page')
def open_specific_Amazon_page(context, specific):
    context.driver.get(f'https://www.amazon.com/gp/product/{specific}/')

@then("Verify product colors")
def verify_product_colors(context):
    color_webelements = context.driver.find_elements(*COLOR_OPTIONS)
    expected_colors=["Medium Wash", "Darck Wash", "Rinse"]
    print(color_webelements)

    for color in color_webelements:
        color.click()
        actual_color = context.driver.find_element(*SELECTED_COLOR).text

    assert actual_color == expected_colors[color_webelements.index(color)]