from browser import Browser
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.products_page = ProductsPage()
    context.cart_page = CartPage()
    context.checkout_page = CheckoutPage()


def before_scenario(context, scenario):
    # Login automat doar pentru scenariile cu tag @products sau @cart
    if "products" in scenario.tags or "cart" in scenario.tags:
        context.login_page.open()
        context.login_page.login("standard_user", "secret_sauce")


def after_all(context):
    context.browser.close()