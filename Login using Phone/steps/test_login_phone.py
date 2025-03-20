from behave import given, when, then
from appium.webdriver.common.appiumby import AppiumBy
from driver import get_driver
import time

# Initialize driver
def get_driver_instance(context):
    if not hasattr(context, 'driver'):
        context.driver = get_driver()
    return context.driver

@given('I launch the Greener Herd app')
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

@when('I click on "Continue with Phone"')
def step_impl(context):
    driver = get_driver_instance(context)
    continueWithPhone = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Continue with Phone")
    time.sleep(2)
    continueWithPhone.click()
    time.sleep(2)

@given("I am on the Login screen")
def step_impl(context):
    driver = get_driver_instance(context)
    time.sleep(2)
    driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="Login"]')
    time.sleep(2)


@when('I see the list of countries and select "{country}"')
def step_impl(context,country):
    driver = get_driver_instance(context)
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'🇦🇪\n+971')
    element.click()
    time.sleep(2)
    search_country_1 = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'🇮🇳\nIndia\n+91')
    assert search_country_1.is_displayed()
    time.sleep(2)
    search_country_2 = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'🇱🇧\nLebanon\n+961')
    assert search_country_2.is_displayed()
    time.sleep(2)
    search_bar = driver.find_element(AppiumBy.XPATH,'//android.widget.EditText')
    search_bar.click()
    time.sleep(2)
    search_bar.send_keys(country)
    time.sleep(2)
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'🇮🇳\nIndia\n+91')
    element.click()
    time.sleep(2)


@then("I verify that India is selected for the phone number")
def step_impl(context):
    driver = get_driver_instance(context)
    India_element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'🇮🇳\n+91')
    time.sleep(2)
    assert India_element.is_displayed()
    time.sleep(2)

@when('I click on the Phone Number field and enter my phone number "{phone}"')
def step_impl(context,phone):
    driver = get_driver_instance(context)
    phoneField = driver.find_element(AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.EditText[1]')
    phoneField.click()
    time.sleep(2)
    phoneField.clear()
    phoneField.send_keys(phone)
    time.sleep(2)


@then('I click on the Password field and enter my password "{password}"')
def step_impl(context,password):
    driver = get_driver_instance(context)
    passwordField = driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="password"]')
    passwordField.click()
    time.sleep(2)
    passwordField.clear()
    passwordField.send_keys(password)
    time.sleep(2)
    driver.hide_keyboard()
    time.sleep(2)


@then("I click on the Login button")
def step_impl(context):
    driver = get_driver_instance(context)
    loginButton = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"on_tap\nLogin")
    time.sleep(2)
    loginButton.click()
    time.sleep(2)

@then("I see error message")
def step_impl(context):
    driver = get_driver_instance(context)

    # Check for error messages
    try:
        errorMsg1 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Incorrect email or password")
        assert errorMsg1.is_displayed(), "Error message 'Incorrect email or password' not displayed."
    except:
        try:
            errorMsg2 = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Password is incorrect")
            assert errorMsg2.is_displayed(), "Error message 'Password is incorrect' not displayed."
        except:
            assert False, "Neither error message found."

    time.sleep(2)
    India_element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'🇮🇳\n+91')
    India_element.click()
    time.sleep(2)
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'🇦🇪\nUnited Arab Emirates\n+971')
    element.click()
    time.sleep(2)


@then("I am directed to the Dashboard page")
def step_impl(context):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Dashboard")
    time.sleep(2)





