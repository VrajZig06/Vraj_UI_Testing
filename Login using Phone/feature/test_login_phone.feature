Feature: Farm Login

Scenario: Launch the App and Navigate to User Registration using Phone
  Given I launch the Greener Herd app
  Then I see the splash screen
  And I see the Welcome popup
  When I click on "Continue with Phone"

#Negative Test Cases
Scenario: Login to the App using Invalid Phone
  Given I am on the Login screen
  When I see the list of countries and select "India"
  Then I verify that India is selected for the phone number
  When I click on the Phone Number field and enter my phone number "7984691564"
  Then I click on the Password field and enter my password "Vraj@123"
  Then I click on the Login button
  Then I see error message

Scenario: Login to the App using Invalid Password
  Given I am on the Login screen
  When I see the list of countries and select "India"
  Then I verify that India is selected for the phone number
  When I click on the Phone Number field and enter my phone number "7984691569"
  Then I click on the Password field and enter my password "Vraj@1234"
  Then I click on the Login button
  Then I see error message

#Positive Test Cases
Scenario: Login to the App using Valid Phone
  Given I am on the Login screen
  When I see the list of countries and select "India"
  Then I verify that India is selected for the phone number
  When I click on the Phone Number field and enter my phone number "7984691569"
  Then I click on the Password field and enter my password "Vraj@123"
  Then I click on the Login button
  Then I am directed to the Dashboard page

