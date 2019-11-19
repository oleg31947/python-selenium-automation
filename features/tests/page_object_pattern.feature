# Created by oleg3 at 11/9/2019
Feature: User wright scenarios to use Page Object pattern

Scenario: Scenario: Logged out user sees Sign in page when clicking Orders
 Given Open Amazon page
 When Click Amazon 'Orders link'
 Then Verify Sign-In page is opened
#=======================================================================================
Scenario: 'Your Shopping Cart is empty' shown if no product added
 Given Open Amazon page
 When Click on cart icon
 Then Verify Your Shopping Cart is empty. text present

#========================================================================================

Scenario: Amazon Music has 6 menu items
 Given Open Amazon page
 When Click on hamburger menu
 And Click on Amazon Music menu item
 Then 6 menu items are present

