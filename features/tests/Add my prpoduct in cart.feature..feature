# Created by oleg3 at 10/16/2019
Feature: User wants to add his product in cart
  # Enter feature description here

  Scenario: Add product in cart
    Given Open Amazon page
    When Search for Sunglasses
    And Open the first product search result
    And Click Add to card button
    Then Verify cart has 1 item.




