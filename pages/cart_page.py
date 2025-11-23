from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from pages.checkout_page import CheckoutPage


CART_PAGE_URL = "https://www.saucedemo.com/cart.html"

class CartPage(BasePage):

    BUTTON_ADD_TO_CART = (By.CLASS_NAME, 'btn_inventory')
    BUTTON_REMOVE_FROM_CART = (By.XPATH, "//button[contains(@class, 'cart_button')]")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")
    CART_ITEM = (By.XPATH, "//div[@class='cart_item']")
    ICON_CART = (By.ID, 'shopping_cart_container')
    BADGE_CART = (By.XPATH, "//span[@class='shopping_cart_badge']")

    def get_products_name_by_index(self, index):
        products = self.driver.find_elements(*self.PRODUCT_NAME)
        return products[index].text

    def get_cart_item_name_by_index(self, index):
        cart_item = self.driver.find_element(*self.CART_ITEM)
        return cart_item[index].text

    def add_item_to_cart(self, index):
        list_all_buttons = self.driver.find_elements(*self.BUTTON_ADD_TO_CART)
        button = list_all_buttons[index]
        button.click()

    def open_cart_page(self):
        self.click(self.ICON_CART)

    def open_checkout_page(self):
        self.click(self.CHECKOUT_BUTTON)

    def remove_items_from_cart(self):
        while True:
            cart_buttons = self.driver.find_elements(*self.BUTTON_REMOVE_FROM_CART)
            if not cart_buttons:
                print("✅ Cart is empty")
                break
            remove_button = self.driver(*self.BUTTON_REMOVE_FROM_CART)
            remove_button.click()
            print("✅ Removed one product from cart")


    def remove_item_from_cart_by_name(self, product_name):
        """Șterge produsul cu numele specificat din cart."""
        items = self.driver.find_elements(*self.CART_ITEM)
        for item in items:
            name = item.find_element(*self.PRODUCT_NAME).text
            if name == product_name:
                item.find_element(*self.REMOVE_BUTTON).click()
                break


    def verify_item_is_added_in_the_cart(self):
        cart_items_number  = len(self.driver.find_elements(*self.CART_ITEM))
        badge_number = int(self.driver.find_element(*self.BADGE_CART).text)
        assert cart_items_number == badge_number, "Cart badge number not match with number of products from the cart!"


    def verify_the_cart_is_empty(self):
        cart_items_number = len(self.driver.find_elements(*self.CART_ITEM))
        assert cart_items_number == 0, "Te product is removed from cart!"


    def verify_product_removed(self, product_name):
        """Verifică că produsul nu mai există în cart și aruncă eroare dacă există."""
        items = self.driver.find_elements(*self.CART_ITEM)
        for item in items:
            name = item.find_element(*self.PRODUCT_NAME).text
            assert name != product_name, f"Produsul '{product_name}' încă există în coș!"


    def verify_new_url(self, expected_url):
        return self.driver.current_url == expected_url


    def items_checkout_step_one(self, index1, index2):
        self.add_item_to_cart(index1)
        self.add_item_to_cart(index2)
        self.open_cart_page()
        self.open_checkout_page()

