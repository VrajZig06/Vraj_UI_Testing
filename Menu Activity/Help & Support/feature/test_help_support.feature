Feature: Menu 
Feature: Menu Page Help & Support

Scenario: Access and interact with the Menu options
    Given I am on the Farm Dashboard page
    When I see the Menu button
    Then I click on the Menu button
    And I am redirected to the Menu page

Scenario: Navigate from menu activity to Help & Support Activity
    Given I am on the Menu Page
    When I should see "Help & Support" button
    Then I click "Help & Support" button
    
Scenario: Filling out Help & Support Form
    Given I am on "Help & Support" Page
    When I should see "Select Category" Field
    Then I click "Select Category" options and Select "Technical Issue"
    When I should see "Query" Field
    Then I click and enter Query details "I have some Login Issues"
    When I should see "Details" Field
    Then I click and enter details "When I enter correct Login credentials then i click on Login but it didn't get login to myAccount instend of it show Loader"
    When I should see "Submit" Field
    Then I click "Submit" button
    Then I redirected to "Dashboard" Page
