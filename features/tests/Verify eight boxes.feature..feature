# Created by oleg3 at 10/18/2019
Feature: Open Amazon prime and verify eight boxes
  # Enter feature description here

  Scenario: Amazon prime page has 8 boxes
    Given Open Amazon page
    When Click on Prime icon
    Then 8 boxes are present
