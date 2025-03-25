Feature: Menu 

Feature: Menu Page Interaction and Verification

  Scenario: Access and interact with the Menu options
    Given I am on the Farm Dashboard page
    When I see the Menu button
    Then I click on the Menu button
    And I am redirected to the Menu page

  Scenario: Verify Menu Options and Clickability
    Given I am on the Menu page
    Then I should see and verify that all options are clickable the following options:

  Scenario: Check for the presence of the Notification button
    Given I am on the Menu page
    When I should see the Notification button

  Scenario: Access and Update My Profile
    Given I am on the Menu Page
    When I see the My Profile button
    Then I click on the My Profile button
    When I am on the My Profile page
    Then I should see my name displayed on the Profile page

  Scenario: Edit Profile Details
    Given I am on the My Profile page
    When I see the "Complete Profile Now" button
    Then I click on the "Complete My Profile" button
    And I am redirected to the Edit My Profile Page

  Scenario: Update Full Name
    Given I am on the Edit My Profile page
    When I see the Full Name field and change name to Vraj
    Then I click Save Button
    And I should see the Personal Details section
    And I should see the Farm Details and Farm Contact Numbers sections
    And I should see the Delete Account and Manage Subscriptions buttons
  