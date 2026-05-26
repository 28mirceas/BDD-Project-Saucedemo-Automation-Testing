from behave import *

@given('Add "{product_name}" to the cart')
def step_add_first_product(context, product_name):
    context.products_page.add_product_to_cart(product_name)


@when('Add "{product_name}" to the cart')
def step_add_second_product(context, product_name):
    context.products_page.add_product_to_cart(product_name)


@when('Enter "{text}" in the first name input field')
def steps_impl(context, text):
    print("CURRENT URL BEFORE FIRST NAME:",
          context.checkout_page.driver.current_url)
    context.checkout_page.set_first_name(text)


@when('Enter "{text}" in the last name input field')
def steps_impl(context, text):
    context.checkout_page.set_second_name(text)


@when('Enter "{text}" in the zip/postal code input field')
def steps_impl(context, text):
    context.checkout_page.set_postal_code(text)


@when('Click to continue button')
def steps_impl(context):
    context.checkout_page.click_continue()
    print("CURRENT URL BEFORE FIRST NAME:",
          context.checkout_page.driver.current_url)


@when('The url of the current page is "{expected_url}"')
def steps_impl(context, expected_url):
    context.login_page.verify_current_url(expected_url)


@then('Verify if sum of the displayed product prices is equal to the total calculated at checkout')
def steps_impl(context):
    context.checkout_page.verify_total_price()
