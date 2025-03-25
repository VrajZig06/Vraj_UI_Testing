Feature: Menu 
Feature: Menu Page Onboard Groups

Scenario: Access and interact with the Menu options
    Given I am on the Farm Dashboard page
    When I see the Menu button
    Then I click on the Menu button
    And I am redirected to the Menu page

Scenario: Onboard Groups Process - Phase 1
    Given I am on the Menu page
    When I see the "Onboard Group" button
    Then I click on the "Onboard Group" option
    When I am redirected to the Group Onboarding page
    Then I should see the "Animal Groups"
    When I see the "Species" dropdown
    Then I click on the "Species" dropdown
    And I select "Cattle" from the list
    Then I click on the "Submit" button
    When I am redirected to the "On-board Groups" page
    Then I should see the "Cattle Group" information
    When I see the "Group Name" field
    Then I click on the "Group Name" field and enter "MY TEST"
    When I see the "Description" field
    Then I click on the "Description" field and enter "Hello, This Group is for General Purpose and for dairy products"
    When I see the "Group Focus" field
    Then I click on the "Group Focus" field and select "General" as the purpose
    When I see the "Production Focus" field
    Then I click on the "Production Focus" field and select "Dairy"
    When I see the "Breed" field
    Then I select "Angus" from the breed list and click "Ok"
    Then I click on the "Next" button

Scenario: Onboard Groups Process - Phase 2
    Given I am on the Age Split page
    When I see the "Age Range" field
    Then I click on the "Age Range" field and select "<2M" and click "Ok"
    Then I click on the "Next" button

Scenario: Onboard Groups Process - Phase 3
    Given I am on the Sex Split page
    When I see the "Sex" field
    Then I click on the "Sex" field and select "Female" and click "Ok"
    Then I click on the "Next" button

Scenario: Onboard Groups Process - Phase 4
    Given I am on the Number of Animals page
    When I see the "Number of Animals" field
    Then I click on the "Number of Animals" field and enter "1"
    Then I click on the "Next" button

Scenario: Onboard Groups Process - Phase 5
    Given I am on the Group Summary page
    When I see the "Group Overview"
    Then I click on the "Submit" button
    Then I am on the Menu page
