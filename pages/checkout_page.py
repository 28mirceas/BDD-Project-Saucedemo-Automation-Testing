from pages.base_page import BasePage
from selenium.webdriver.common.by import By

CHECKOUT_PAGE_URL = "https://www.saucedemo.com/checkout-step-one.html"

class CheckoutPage(BasePage):

    INPUT_FIRST_NAME = (By.ID, "first-name")
    INPUT_LAST_NAME = (By.ID, "last-name")
    INPUT_POSTAL_CODE = (By.ID, "postal-code")
    BUTTON_CONTINUE = (By.ID, "continue")
    CHECKOUT_ITEM_PRICE = (By.XPATH, "//div[@class='inventory_item_price']")
    TOTAL_PRICE = (By.XPATH, "//div[@class='summary_subtotal_label']")

    def set_first_name(self, text):
        self.type(self.INPUT_FIRST_NAME, text)

    def set_second_name(self, text):
        self.type(self.INPUT_LAST_NAME, text)

    def set_postal_code(self, text):
        self.type(self.INPUT_POSTAL_CODE, text)

    def click_continue(self):
        self.click(self.BUTTON_CONTINUE)

    def verify_total_price(self):
        list_all_checkout_items = self.driver.find_elements(*self.CHECKOUT_ITEM_PRICE)
        list_all_checkout_items_price = []

        for item in list_all_checkout_items:
            price = item.text.replace("$", "")
            list_all_checkout_items_price.append(float(price))

        total_price = self.driver.find_element(*self.TOTAL_PRICE).text
        total_price = float(total_price.replace("Item total: $", ""))
        assert round(sum(list_all_checkout_items_price), 2) == round(total_price, 2), (
            f"Expected total {sum(list_all_checkout_items_price)}, but found {total_price}"
        )

