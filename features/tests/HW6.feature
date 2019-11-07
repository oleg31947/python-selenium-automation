# Created by oleg3 at 11/5/2019
Feature: Open and close many windows.
  User open few windows and add product in a cart.

  Scenario: User open few windows and aDd product in a cart.
    Given Open Amazon page
    When Store original window
    When Click to open deals under $25
    And Switch to the new opened window
    Then Shop all deals are shown.
    When Put Headphones into a cart
    And Close new window, switch back to original
    And Refresh the page
    Then Verify cart has 1 item.