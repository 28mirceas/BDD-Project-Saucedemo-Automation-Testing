Feature: Verify the functionality of the checkout page

  @cart
  @totalPrice
  @flaky
  Scenario: Verify total price of the cart products
    Given Add "Sauce Labs Backpack" to the cart
    When Add "Sauce Labs Bike Light" to the cart
    And Click to cart icon
    And Click to checkout button
    And Enter "John" in the first name input field
    And Enter "Doe" in the last name input field
    And Enter "01234" in the zip/postal code input field
    And Click to continue button
    And The url of the current page is "https://www.saucedemo.com/checkout-step-two.html"
    Then Verify if sum of the displayed product prices is equal to the total calculated at checkout
