Feature: Navigate from Dashboard to Marketplace Feed and Marketplace Page


  Scenario: Navigate from Dashboard to Marketplace Feed
    Given I am on the Dashboard Page
    Then I should see all 5 menus displayed
    Then I should see the Marketplace button displayed
    When I click on the Marketplace button
    Then I should be redirected to the Marketplace Page


 Scenario: Apply a filter to products
    Given I am on the "Marketplace Feeds" activity
    When I should see the "Filter" button
    Then I click on the "Filter" button
    Then I should see the filter pop-up screen
    When I select "Product Type" as "fodder" and "Animal Species" as "Cattle"
    Then I should see the "Apply Filter" button
    When I click on the "Apply Filter" button
    Then I should see a first product named as Alfa Alfa

  Scenario: Removing all filters
    Given I am on the "Marketplace Feeds" activity
    When I should see the "Filter" button
    Then I click on the "Filter" button
    Then I should see the filter pop-up screen
    When I should see the "Remove Filters" button
    Then I click on the "Remove Filters" button
    Then I should see the first item as "500kg beef"


  Scenario: When user clicks on a particular product
    Given I am on the "Marketplace Feeds" activity
    When I should see the first product in the product list
    Then I click on the first product
    Then I will be redirected to the "View Product Detail" page
    When I see the detail of "500 kg Beef Calf Mix"
    Then I should see the price of that product
    When I should see the "Nutritional Composition" section
    Then I should see the following items in the nutritional section:
    When I should see the "Supplier Details" section
    Then I should see the following items in the supplier section:
    When I should see the "Feeding Instructions" section
    Then I should see the back button on the top left side
    When I click on the back button
    Then I should be redirected back to the "Marketplace Feeds" activity


  Scenario: Search product
    Given I am on the "Marketplace Feeds" activity
    Then I should see the Search bar and Filter button
    Then I should see the Notification button
    Then I should see a list of products displayed
    When I Enter product name to Search bar 'Corn - raw'
    Then I should see the Corn - raw Product