from behave import *

@when('Enter "{text}" in the first name input field')
def steps_impl(context, text):
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

@then('Verify if sum of the displayed product prices is equal to the total calculated at checkout')
def steps_impl(context):
    context.checkout_page.verify_total_price()
