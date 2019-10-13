# Created by oleg3 at 10/12/2019
Feature: Tests for Cancel orders


  Scenario: User can search for Cancelling an order on Amazon
    Given Open Amazon Help page
    When Tipe Cancel order
    Then Verify Help page is opened
