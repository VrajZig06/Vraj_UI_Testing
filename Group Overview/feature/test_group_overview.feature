Feature: Group Overview

  Scenario: Group Overview
    Given I am on the Dashboard page
    Then I should see the "Group Overview" button
    When I click on the "Group Overview" button
    Then I should be redirected to the "Group Overview" page
    And I should be able to view the group list and clickable
    When I click on the first group in the group list : Group Id :- "hello ‪(1)"
    Then I should be redirected to the "Group Details" page and Verify Same Group Detail : Group Id :- "hello  ‪(1)"
    Then I should see the following elements
      | Animal tag number search bar |
      | Group name                   |
      | Description                  |
      | Group focus                  |
      | List of animals              |
      | Upcoming tasks               |
    And I should see the "Notification" button