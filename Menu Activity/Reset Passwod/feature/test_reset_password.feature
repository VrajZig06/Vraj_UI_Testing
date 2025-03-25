Feature: Menu 
Feature: Menu Page Reset Password

Scenario: Access and interact with the Menu options
    Given I am on the Farm Dashboard page
    When I see the Menu button
    Then I click on the Menu button
    And I am redirected to the Menu page

# Positive Scenario
Scenario: Reset Password Process
    Given I am on the Menu Page
    When I should see the Reset Password Button
    Then I click on Reset Password button
    Then I am redirected to the Reset Password Page
    When I should see the two input fields "Old Password" and "New Password"
    Then I click on the "Old Password Field" and then I entered Old Password : "Vraj@123"
    Then I click on the "New Password Field" and then I entered New Password : "Vraj@123"
    When I should see the Submit Button
    Then I click on that Submit Button
    Then I am on the Dashboard
    Then I should see the menu option and click menu
    
# Negative Scenario
Scenario: Reset Password with wrong old password
    Given I am on the menu Page
    When I should see the Reset Password Button
    Then I click on Reset Password button
    Then I am redirected to the Reset Password Page
    When I should see the two input fields "Old Password" and "New Password"
    Then I click on the "Old Password Field" and then I entered wrong Old Password : "Test@123"
    Then I click on the "New Password Field" and then I entered New Password : "Vraj@123"
    When I should see the Submit Button
    Then I click on that Submit Button
    Then I am redirected to the Reset Password Page
