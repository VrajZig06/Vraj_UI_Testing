Feature: Farm Login

Scenario: Launch the App and Navigate to User Registartion using Phone
  Given I click on Greener Herd app
  Then I see the splash screen
  And I see the Welcome popup
  When I Click on Continue with Email  
  
Scenario: Login to App using email
  Given I am at Login Activity
  When I Click on Email Field and I Enter my Email vrajm@zignuts.com
  Then I click on password Field and I Enter my password Vraj@123
  Then I click on Login Button 
  Then I am at dashboard Page
 
