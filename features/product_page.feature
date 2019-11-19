# Created by oleg3 at 11/16/2019
Feature: Test for product page
  # Enter feature description here

  Scenario: Fashion tooltip is shown upon hovering over Add To Cart
    Given Open gp/product/B074TBCSC8 Amazon page
    When Hover over SALES & DEALS
    Then Verify fashion tooltip is shown


  Scenario: User can select department
    Given Open Amazon page
    When Select CDs & Vinyl department
    And Search for The Beatles The White Album
    Then CDs & Vinyl department is selected
