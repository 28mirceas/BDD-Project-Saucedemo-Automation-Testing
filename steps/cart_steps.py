from behave import *

@given('Add product number {index} to the cart')
def step_impl(context, index):
    index = int(index)
    context.cart_page.add_item_to_cart(index)

@when('Add product number {index} to the cart')
def step_impl(context, index):
    index = int(index)
    context.cart_page.add_item_to_cart(index)


@when('Click to cart icon')
def step_impl(context):
    context.cart_page.open_cart_page()


@when('Click to checkout button')
def step_impl(context):
    context.cart_page.open_checkout_page()


@then('Verify the product is added in the cart')
def step_impl(context):
    context.cart_page.verify_item_is_added_in_the_cart()

@when('Remove the product from the cart')
def step_impl(context):
    context.cart_page.remove_items_from_cart()

@when('Remove product "{text}" from the cart')
def step_impl(context, text):
    context.cart_page.remove_item_from_cart_by_name(text)

@then('Verify the cart is empty')
def step_impl(context):
    context.cart_page.verify_the_cart_is_empty()

@then('Verify if product "{text}" is removed from cart')
def step_impl(context, text):
    context.cart_page.verify_product_removed(text)


# @then('The url of the current page is "{expected_url}"')
# def steps_impl(context, expected_url):
#     context.login_page.verify_current_url(expected_url)


@then('The current url should be "{new_url}"')
def steps_impl(context, new_url):
    context.cart_page.verify_new_url(new_url)
