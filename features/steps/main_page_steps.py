

@Then('Verify cart has {expected_item_count} item')
def verify_item_count(context, expected_item_count):
    sleep(3)
    actual_items = context.driver.find_elemrnt(*CARD_ITEM_COUNT).text
    assert actual_items == expected_item_count, f'Expected {expected_item_count}, but got {actual_items}'


