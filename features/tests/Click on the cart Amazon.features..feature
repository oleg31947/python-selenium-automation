# Created by oleg3 at 10/13/2019
Feature: Test for clicks on the cart icon
  # Enter feature description here

  Scenario: Ucer click on the cart icon
    Given Open Amazon page
    When Click on the cart icon
    Then Verify Cart page open #Enter feature name here
