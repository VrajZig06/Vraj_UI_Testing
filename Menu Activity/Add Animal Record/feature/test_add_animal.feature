Feature: Menu 
Feature: Menu Page Add New Animal

Scenario: Access and interact with the Menu options
    Given I am on the Farm Dashboard page
    When I see the Menu button
    Then I click on the Menu button
    And I am redirected to the Menu page

Scenario: Navigate from menu activity to Add Animal Record Activity
    Given I am on the Menu Page
    When I should see "Add New Animal" option
    Then I click on "Add Animal Record" option

Scenario: Add Animal Record - Phase 1
    Given I am on the Add Animal Record Page
    When I should see Purchase Information 
    Then I should see two Dropdown box "Add Animal Species" and "Add Animal Source"
    Then I click on "Add Animal Species" and select "Cattle" as Species
    Then I click on "Add Animal Source" and select "Purchased" as Animal Source
    Then I click on "Next" button

Scenario: Add Animal Record - Phase 2
    Given I am on Purchase Information Page
    When I should see Following Fields
    Then I click "Seller Name" Field and enter seller name "Virat"
    Then I click "Price Paid" Field and enter price paid value "2000"
    Then I click "Combined Weight" and enter weight "200"
    Then I click "Number of Animals" and enter animal count as "1"
    Then I click "Production Focus" and select "Dairy"
    Then I click "select date of Purchase" and click on "Ok" button
    Then I click on "Next" button

Scenario: Add Animal Record - Phase 3
    Given I am on "Animal Information" Page
    When I should see "Add Animal Photo" Field
    Then I click on "Add Animal Photo" and select "Camera" option
    Then I click on "Shutter" button and then I click on "Correct" option
    When I should see "Tag Number" Field
    Then I click "Tag Number" Field and Enter Tag Number "TestCow1"
    When I should see "Breed" Field 
    Then I click on "Breed" and select "Angus" 
    When I should see "Name" Field 
    Then I click on "Name" and enter "Cowhsa"
    When I should see "Age" Field 
    Then I click on "Age" and enter "10"
    When I should see "Sex" Field 
    Then I click "Sex" and select "Female"
    When I should see "Birth Weight" Field
    Then I click "Birth Weight" and enter "200"
    When I should see "Breeding Stage" Field
    Then I click "Breeding Stage" and select "First breeding"
    When I should see "Dam", "Sire" and "Documents" Fields
    Then I click "date of birth" and click "Ok"
    Then I click on "Next" button

Scenario: Add Animal Record - Phase 4
    Given I am on "Animal Added" Page
    Then I click on "Next" button

Scenario: Add Animal Record - Phase 5
    Given I am on "Allocate to a Group" page
    When I should see "CheckBox with my Animal" 
    Then I check that CheckBox
    Then I click on "Next" button

Scenario: Add Animal Record - Phase 6   
    Given I am on "Add to Group" Page
    When I should see Two options "Recommended Group" and "Create a new Group"
    Then I click "Recommended Group" and select group "New data"
    Then I click "Submit button"
    