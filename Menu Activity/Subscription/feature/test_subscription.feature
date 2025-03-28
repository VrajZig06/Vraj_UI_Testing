Feature: Subscription 

Scenario: Launch the App and Navigate to User Registartion using Phone
    Given I click on Greener Herd app
    Then I see the splash screen
    And I see the Welcome popup
    When I Click on Continue with Email  

Scenario: Login to App using email
    Given I am at Login Activity
    When I Click on Email Field and I Enter my Email drashti@yopmail.com
    Then I click on password Field and I Enter my password Test@1234
    Then I click on Login Button 
    Then I am at dashboard Page
  
Scenario: Navigate from Dashboard to Menu Page
    Given I am on the Dashboard Page
    When I see the "Menu" button
    Then I click on the "Menu" button
    Then I should be redirected to the Menu Page      

Scenario: Navigate from Menu Page to Profile Page
    Given I am on the Menu Page
    When I see the "My Profile" option
    Then I click on the "My Profile" button
    Then I should be redirected to the My Profile Page

Scenario: Process from My Profile Page to Subscription Page
    Given I am on the My Profile Page
    When I see the "Subscription Plan" details at the bottom of the Profile Page
    Then I verify the subscription plan is "Trial Plan"
    When I see the "Manage Subscription" button
    Then I click on the "Manage Subscription" button
    Then I should be redirected to the Manage Subscription Page

Scenario: Verify Manage Subscription Page Features
    Given I am on the Manage Subscription Page
    When I see the "Features Description" at the top of the screen
    Then I verify that "Limited Offer" is displayed
    When I see all available subscription plans listed below
    When I verify that the "Select Plan and Subscribe" button is visible
    Then I click on "Pay ₹4,600.00" button
    Then I should see PopUp Box

