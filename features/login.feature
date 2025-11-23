Feature: Test the login functionality

  Background: Open the login page
     Given Navigate to login page

  @login
  Scenario: Login as standard user with valid credentials
    When  Enter "standard_user" in the username input field
    And Enter "secret_sauce" in the password input field
    And Click the login button
    Then The url of the current page is "https://www.saucedemo.com/inventory.html"

