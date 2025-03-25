Feature: Menu 
Feature: Menu Page Record Animal Sale

Scenario: Access and interact with the Menu options
    Given I am on the Farm Dashboard page
    When I see the Menu button
    Then I click on the Menu button
    And I am redirected to the Menu page

Scenario: Redirects from menu to Record Animal Sale Activity
    Given I am on the Menu page
    When I should see the Record Animal Sale option
    Then I click on the Record Animal Sale option
    Then I am redirect to Animal Selling Record

Scenario: Filling all Details for Sale Animal
    Given I am on the Animal Selling page
    When I see the 3 stages at the top of the app
    Then I should be redirected to the "1" stage of the Animal Selling Activity
    Then I should see the Sell Information section
    When I see the "Add Animal Species" option
    Then I click on the "Add Animal Species" option
    And I select the first option "Cattle"
    When I see the "Purchaser Name" option
    Then I click on the "Purchaser Name" option
    And I enter the name "Vraj"
    When I see the "Select Date to Sell" option
    Then I click on the calendar button and select a date
    When I see the "Number of Animals" option
    Then I click on the option and enter the number of animals "1"
    When I see the "Price Paid" option
    Then I click on the "Price Paid" option and enter the price "200"
    When I see the "Weight" option
    Then I click on the "Weight" option and enter the weight "500"
    When I see the "Next" button
    When I click Next button
    Then I should be redirected to the "2" stage of the Animal Selling Activity
    When I see the "Enter Animal Tag Number" option
    Then I click on "Enter Animal Tag Number" option
    When I see the "Search Bar" option
    Then I click on the search bar and enter the tag number "Yahooo"
    When I see the "Next" button
    Then I click on the "Next" button
    Then I should be redirected to the "3" stage of the Animal Selling Activity
    Then I Should see the details of my sale Animal Details "Yahooo"
    When I see the "Next" button
    Then I click on the "Next" button
    Then I redirect to the Dashboard Page