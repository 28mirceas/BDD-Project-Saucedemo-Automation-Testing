from pages.base_page import BasePage
from selenium.webdriver.common.by import By

PRODUCTS_PAGE_URL = "https://www.saucedemo.com/inventory.html"

class ProductsPage(BasePage):

    ITEM_PRICE = (By.CLASS_NAME, 'inventory_item_price')
    ITEM_NAME = (By.CLASS_NAME, 'inventory_item_name')
    DROPDOWN_SORT = (By.CLASS_NAME, 'product_sort_container')

    def __init__(self, driver):
        super().__init__(driver)


    def select_dropdown(self, text):
        self.select_item_by_text(self.find(self.DROPDOWN_SORT), text)


    def verify_product_price_sorted_low_to_high(self):
        list_all_items = self.find_multiple(self.ITEM_PRICE)
        list_all_items_price = []

        for item in list_all_items:
            price = item.text.replace("$", "").strip()
            list_all_items_price.append(float(price))

        expected = sorted(list_all_items_price)
        assert list_all_items_price == expected, f"Price not sorted: {list_all_items_price}"


    def verify_product_name_sorted_z_to_a(self):
        list_all_items = self.find_multiple(self.ITEM_NAME)
        list_all_items_name = []

        for item in list_all_items:
           list_all_items_name.append(item.text)

        expected = sorted(list_all_items_name, reverse=True)
        assert list_all_items_name == expected, f"Name not sorted: {list_all_items_name}"
        

    def add_product_to_cart(self, product_name):
        locator = (
            By.XPATH,
            f"//div[contains(@class,'inventory_item_name') and normalize-space(text())='{product_name}']"
            "/ancestor::div[contains(@class,'inventory_item')]"
            "//button"
        )
        self.click(locator)
