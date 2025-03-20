Feature: Farm Dashboard

Scenario: Verify Dashboard Page Elements
  Given I am on the Farm Dashboard page
  When I see the group of animals displayed in different species
  Then I should see the Animal Tag Number search bar
  Then I should see "My Herd" section
  Then I should see the status overview section
  Then I should see the AVG FCR (Average Feed Conversion Ratio) displayed
  Then I should see the Average Daily Gain section
  Then I should see the Average Calf Weight section
  Then I should see the Emission overview section
  Then I should see the Feed overview section
  Then I should see the Weather Forecast section
  Then I should also see the Notification button
  Then I Should also see then Dashboard Button