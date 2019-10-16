# Created by oleg3 at 10/13/2019
Feature: Test for clicks on the cart icon
  # Enter feature description here

  Scenario: Ucer click on"a#nav-cart" the cart icon
    Given Open Amazon page
    When Click on the card icon
    Then Verifies that Your Shopping Cart is empty
