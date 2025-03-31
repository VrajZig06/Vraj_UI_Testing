Feature: Subscription 



Scenario: Verify Manage Subscription Page Features -- Update Version
    Given I am on the Manage Subscription Page
    When I see the "Features Description" at the top of the screen
    When I see all available subscription plans listed below
    When I verify that the "Select Plan and Subscribe" button is visible
    Then I click on "Pay ₹4,600.00" button
    Then I should see PopUp Box
    When I should see "Subscribe" button
    Then I click on "Subscribe" button
    And I should see "Subscribed Successfull" Message
    