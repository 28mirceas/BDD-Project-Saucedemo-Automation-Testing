Feature: Verify the functionality of the products page


  @products
  @productsPrice
  Scenario: Verify products are sorted by price (low to high)
    Given I sort the products by price "Price (low to high)"
    When Products are sorted by price - low to high


  @products
  @productsName
  Scenario: Verify products are sorted by name (Z to A)
    Given I sort the products by name "Name (Z to A)"
    When Products are sorted by name - Z to A


