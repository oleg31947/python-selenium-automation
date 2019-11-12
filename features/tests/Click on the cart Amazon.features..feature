# Created by oleg3 at 10/13/2019
Feature: Test for clicks on the cart icon
  # Enter feature description here

  Scenario: User click on"a#nav-cart" the cart icon
    Given Open Amazon page
    When Click on cart icon
    Then Verify Your Shopping Cart is empty. text present
