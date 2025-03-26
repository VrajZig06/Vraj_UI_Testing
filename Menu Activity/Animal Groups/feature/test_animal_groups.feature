Feature: Menu 
Feature: Menu Page Animal Groups

Scenario: Access and interact with the Menu options
    Given I am on the Farm Dashboard page
    When I see the Menu button
    Then I click on the Menu button
    And I am redirected to the Menu page

Scenario: Navigate from menu activity to Animal Groups Activity
    Given I am on the Menu Page
    When I should see "Animal Groups" button
    Then I click "Animal Groups" button
    Then I am on Dashboard Page