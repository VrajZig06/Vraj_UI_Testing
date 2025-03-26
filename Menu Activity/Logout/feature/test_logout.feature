Feature: Menu 
Feature: Menu Page Logout


Scenario: Access and interact with the Menu options
    Given I am on the Farm Dashboard page
    When I see the Menu button
    Then I click on the Menu button
    And I am redirected to the Menu page

Scenario: Navigate from menu activity to logout process
    Given I am on the Menu Page
    When I should see "Logout" button
    Then I click "Logout" button    
    When I should see Logout Popup
    Then I click on "Logout" button
    Then I should see "Welcome to Greenerherd" Popup