from behave import given, when, then
from appium.webdriver.common.appiumby import AppiumBy
from driver import get_driver
import time

# Initialize driver
def get_driver_instance(context):
    if not hasattr(context, 'driver'):
        context.driver = get_driver()
    return context.driver

@given('I click on Greener Herd app')
def step_impl(context):
    driver = get_driver_instance(context)
    element = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Greener Herd"]')
    element.click()
    time.sleep(1)

@then('I see the splash screen')
def step_impl(context):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView')
    time.sleep(5)

@then('I see the Welcome popup')
def step_impl(context):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Welcome to\nGreener Herd')
    time.sleep(2)

@when("I Click on Continue with Email")
def step_impl(context):
    driver = get_driver_instance(context)
    continueWithPhone = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Continue with Email")
    time.sleep(2)
    continueWithPhone.click()
    time.sleep(2)

@given("I am at Login Activity")
def step_impl(context):
    driver = get_driver_instance(context)
    time.sleep(2)
    driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="Login"]')
    time.sleep(5)


@when("I Click on Email Field and I Enter my Email {email}")
def step_impl(context,email):
    driver = get_driver_instance(context)
    emailField = driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="email address"]')
    emailField.click()
    time.sleep(2)
    emailField.send_keys(email)
    time.sleep(2)
    driver.hide_keyboard()
    time.sleep(2)


@then("I click on password Field and I Enter my password {password}")
def step_impl(context,password):
    driver = get_driver_instance(context)
    passwordField = driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="password"]')
    time.sleep(2)
    passwordField.click()
    time.sleep(2)
    passwordField.send_keys(password)
    time.sleep(2)
    driver.hide_keyboard()
    time.sleep(2)


@then("I click on Login Button")
def step_impl(context):
    driver = get_driver_instance(context)
    loginButton = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"on_tap\nLogin")
    time.sleep(2)
    loginButton.click()
    time.sleep(2)

@then("I am at dashboard Page")
def step_impl(context):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Dashboard")
    time.sleep(2)
