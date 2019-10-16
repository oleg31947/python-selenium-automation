# Created by oleg3 at 10/12/2019
Feature: Tests for Cancel orders


  Scenario: User can search for Cancelling an order on Amazon
    Given Open Amazon Help
    When Input Cancel order into search field
    And Click on search icon
    Then Verify Cancel Order page is opened
