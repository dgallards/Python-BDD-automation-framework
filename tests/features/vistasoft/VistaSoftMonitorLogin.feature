@web
Feature: Login feature for VistaSoft Monitor IoT Solution
  
  Background: Login to VS Monitor System
    Given I am on "https://vsmonitor.com" - VS Monitor Homepage
    When I click on Login button in VS Monitor Homepage
    Then I validate that I navigate to Login page

  @totest
  @LoginWithIncorrectCredential
  Scenario: Login with incorrect credential to VS Monitor Homepage
    Given I enter "abc@gmail.com" for username and "123456789" for password
    When I click on LOG-IN button on Log-in page
    Then I verify that the "Invalid username or password." should be displayed


  @LoginWithCorrectCredential
  Scenario: Login with correct credential to VS Monitor Homepage
    Given I enter "nmw_ng@hotmail.com" for username and "meewai123" for password
    When I click on LOG-IN button on Log-in page
    Then I verify that I able to navigate to Dashboard at "https://vsmonitor.com/dashboard"


