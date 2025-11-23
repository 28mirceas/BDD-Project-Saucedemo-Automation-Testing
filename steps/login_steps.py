from behave import given, when, then

@given('Navigate to login page')
def steps_impl(context):
    context.login_page.open()

@when('Enter "{user_text}" in the username input field')
def steps_impl(context, user_text):
    context.login_page.set_username(user_text)

@when('Enter "{pass_text}" in the password input field')
def steps_impl(context, pass_text):
    context.login_page.set_password(pass_text)

@when('Click the login button')
def steps_impl(context):
    context.login_page.click_button()

@then('The url of the current page is "{expected_url}"')
def steps_impl(context, expected_url):
    context.login_page.verify_current_url(expected_url)