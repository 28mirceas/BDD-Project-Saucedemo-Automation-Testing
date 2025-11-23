Feature: Verify the functionality of the cart page

  @cart
  @addToCart
  Scenario: Add the third product in the shopping cart
    Given Add product number 3 to the cart
    When Click to cart icon
    Then Verify the product is added in the cart


  @cart
  @addRemoveProductFromCart
    Scenario: Add product in the shopping card then and remove it from the shopping cart
    Given Add product number 2 to the cart
    When Click to cart icon
    And Remove the product from the cart
    Then Verify the cart is empty


  @cart
  @removeOneProductFromCart
    Scenario: Add more products in the shopping cart and remove one product from shopping cart
    Given Add product number 1 to the cart
    When Add product number 3 to the cart
    And Click to cart icon
    And Remove product "Sauce Labs Bolt T-Shirt" from the cart
    Then Verify if product "Sauce Labs Bolt T-Shirt" is removed from cart
  

  @cart
  @checkoutFlow
    Scenario: Navigate to checkout page
    Given Add product number 4 to the cart
    When Click to cart icon
    And Click to checkout button
    Then The current url should be "https://www.saucedemo.com/checkout-step-one.html"





