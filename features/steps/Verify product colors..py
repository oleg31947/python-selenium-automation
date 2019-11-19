
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

COLOR_OPTIONS = (By.CSS_SELECTOR, "div#variation_color_name li")
SELECTED_COLOR = (By.CSS_SELECTOR, "div#variation_color_name .selection")


@then("Verify product colors")
def verify_product_colors(context):
    color_webelements = context.driver.find_elements(*COLOR_OPTIONS)
    expected_colors = ["Medium Wash", "Dark Wash", "Rinse"]
    print(color_webelements)

    for color in color_webelements:
        color.click()
        actual_color = context.driver.find_element(*SELECTED_COLOR).text

    assert actual_color == expected_colors[color_webelements.index(color)]

#=========================================================================















