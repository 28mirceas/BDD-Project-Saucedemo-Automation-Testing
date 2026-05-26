from pages.base_page import BasePage
from selenium.webdriver.common.by import By

CHECKOUT_PAGE_URL = "https://www.saucedemo.com/checkout-step-one.html"

class CheckoutPage(BasePage):

    INPUT_FIRST_NAME = (By.ID, "first-name")
    INPUT_LAST_NAME = (By.ID, "last-name")
    INPUT_POSTAL_CODE = (By.ID, "postal-code")
    BUTTON_CONTINUE = (By.ID, "continue")
    CHECKOUT_ITEM_PRICE = (By.XPATH, "//div[@data-test='inventory-item-price']")
    TOTAL_PRICE = (By.XPATH, "//div[@data-test='subtotal-label']")


    def __init__(self, driver):
        super().__init__(driver)


    def set_first_name(self, text):        
        element = self.find(self.INPUT_FIRST_NAME)        
        element.clear()
        element.send_keys(text)


    def set_second_name(self, text):
        element = self.find(self.INPUT_LAST_NAME)       
        element.clear()
        element.send_keys(text)
        

    def set_postal_code(self, text):
        element = self.find(self.INPUT_POSTAL_CODE)
        element.click()
        element.clear()
        element.send_keys(text)

       
    def click_continue(self):       
        self.click(self.BUTTON_CONTINUE)     


    def verify_total_price(self):
        list_all_checkout_items = self.find_multiple(self.CHECKOUT_ITEM_PRICE)

        list_all_checkout_items_price = []

        for item in list_all_checkout_items:
            price = item.text.replace("$", "").strip()
            list_all_checkout_items_price.append(float(price))

        total_price_text = self.find(self.TOTAL_PRICE).text

        total_price = float(
            total_price_text
            .replace("Item total:", "")
            .replace("$", "")
            .strip()
        )

        calculated_total = round(sum(list_all_checkout_items_price), 2)
        ui_total = round(total_price, 2)

        assert abs(calculated_total - ui_total) < 0.01, (
            f"Expected total {calculated_total}, but found {ui_total}"
        )

