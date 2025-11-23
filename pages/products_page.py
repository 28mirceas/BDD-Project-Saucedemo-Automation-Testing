from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

PRODUCTS_PAGE_URL = "https://www.saucedemo.com/inventory.html"

class ProductsPage(BasePage):

    ITEM_PRICE = (By.CLASS_NAME, 'inventory_item_price')
    ITEM_NAME = (By.CLASS_NAME, 'inventory_item_name')
    DROPDOWN_SORT = (By.CLASS_NAME, 'product_sort_container')


    def select_dropdown_item(self, text):
        dropdown = Select(self.find(self.DROPDOWN_SORT))
        dropdown.select_by_visible_text(text)


    def verify_product_price_sorted_low_to_high(self):
        list_all_items = self.driver.find_elements(*self.ITEM_PRICE)
        list_all_items_price = []

        for item in list_all_items:
            price = item.text.replace("$", "")
            list_all_items_price.append(float(price))

        assert list_all_items_price == sorted(list_all_items_price)


    def verify_product_name_sorted_z_to_a(self):
        list_all_items = self.driver.find_elements(*self.ITEM_NAME)
        list_all_items_name = []

        for item in list_all_items:
           list_all_items_name.append(item.text)

        assert list_all_items_name ==  sorted(list_all_items_name,reverse = True)