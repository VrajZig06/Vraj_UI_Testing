Feature: Menu 
Feature: Menu Page My feed Inventory

Scenario: Access and interact with the Menu options
    Given I am on the Farm Dashboard page
    When I see the Menu button
    Then I click on the Menu button
    And I am redirected to the Menu page

Scenario: Navigate from menu activity to My Feed Inventory Activity
    Given I am on the Menu Page
    When I should see "My Feed Inventory" button
    Then I click "My Feed Inventory" button

Scenario: My Feed Inventory Page
    Given I am on "My Feed Inventory" Page
    When I should see "Alfalfa" Feed in my List
    Then I should see "Add New Product" button
    Then I should see "Update" Button

Scenario: Update Existing Feed 
    Given I am on "My Feed Inventory" Page
    When I should see "Update" Button of any Particular Object
    Then I click "Update" Button
    And I see Update Popup is Open
    Then I click on "Weight" field and Enter Update value "300"
    Then I click on "Purchase Cost" and Enter Update value "30"
    Then I click "Update Inventory" button

Scenario: Add New Product to My Inventory    
    Given I am on "My Feed Inventory" Page
    When I click "Add New Product" button
    Then I should see "Add New Product" Popup
    Then I click "Product Type" and Select "Fodder"
    Then I click "Find Product" and Select "Alfalfa"
    Then I click "Supplier" and Select "Aidco"
    Then I click "Weight" and Enter Weight as "200"
    Then I click "Purchase Cost" and Enter Cost as "2000"
    Then I click "Add to Feed" button