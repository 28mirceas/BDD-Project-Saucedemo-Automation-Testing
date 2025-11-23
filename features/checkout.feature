Feature: Verify the functionality of the checkout page

  @cart
  @totalPrice
  Scenario: Verify total price of the cart products
    Given Add product number 2 to the cart
    When Add product number 5 to the cart
    And Click to cart icon
    And Click to checkout button
    And Enter "John" in the first name input field
    And Enter "Doe" in the last name input field
    And Enter "01234" in the zip/postal code input field
    And Click to continue button
    Then Verify if sum of the displayed product prices is equal to the total calculated at checkout