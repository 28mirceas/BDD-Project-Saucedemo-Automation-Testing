from behave import *

@given('I sort the products by price "{text}"')
def step_impl(context, text):
    context.products_page.select_dropdown_item(text)


@when('Products are sorted by price - low to high')
def step_impl(context):
    context.products_page.verify_product_price_sorted_low_to_high()


@given('I sort the products by name "{text}"')
def steps_impl(context, text):
    context.products_page.select_dropdown_item(text)

@when('Products are sorted by name - Z to A')
def steps_impl(context):
    context.products_page.verify_product_name_sorted_z_to_a()