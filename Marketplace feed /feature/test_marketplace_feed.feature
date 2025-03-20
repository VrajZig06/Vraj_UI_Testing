Feature: Navigate from Dashboard to Marketplace Feed and Marketplace Page

Scenario: Navigate from Dashboard to Marketplace Feed
  Given I am on the Dashboard Page
  Then I should see all 5 menus displayed
  Then I should see the Marketplace button displayed
  When I click on the Marketplace button
  Then I should be redirected to the Marketplace Page
  Then I should see the Search bar and Filter button
  Then I should see the Notification button
  Then I should see a list of products displayed
  When I Enter product name to Search bar 'Corn - raw'

  
