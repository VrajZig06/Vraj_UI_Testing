from behave import given, when, then
from appium.webdriver.common.appiumby import AppiumBy
from driver import get_driver
import time
import datetime

# Initialize driver
def get_driver_instance(context):
    if not hasattr(context, 'driver'):
        context.driver = get_driver()
    return context.driver


def scroll_down(driver):
    driver.execute_script("mobile: scrollGesture", {
        "left": 100, "top": 0, "width": 200, "height": 700,
        "direction": "down",
        "percent": 1.0
    })


@given('I am on the Farm Dashboard page')
def step_impl(context):
    driver = get_driver_instance(context)
    dashboard = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Dashboard')
    assert dashboard.is_displayed()
    time.sleep(2)

@when("I see the Menu button")
def step_impl(context):
    driver = get_driver_instance(context)
    menuBtn = driver.find_element(AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.ImageView[4]')
    assert menuBtn.is_displayed()
    time.sleep(2)

@then('I click on the Menu button')
def step_impl(context):
    driver = get_driver_instance(context)
    menuBtn = driver.find_element(AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.ImageView[4]')
    menuBtn.click()
    time.sleep(2)

@then('I am redirected to the Menu page')
def step_impl(context):
    driver = get_driver_instance(context)
    menuPage = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Menu')
    assert menuPage.is_displayed()
    time.sleep(2)

@given('I am on the Menu page')
def step_impl(context):
    driver = get_driver_instance(context)
    menuPage = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Menu')
    assert menuPage.is_displayed()
    time.sleep(2)

@when('I should see the Reset Password Button')
def step_impl(context):
    driver = get_driver_instance(context)
    menuPage = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Reset Password')
    assert menuPage.is_displayed()
    time.sleep(2)


@then('I click on Reset Password button')
def step_impl(context):
    driver = get_driver_instance(context)
    menuPage = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Reset Password')
    menuPage.click()
    time.sleep(2)

@then('I am redirected to the Reset Password Page')
def step_impl(context):
    driver = get_driver_instance(context)
    menuPage = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Reset Password')
    assert menuPage.is_displayed()
    time.sleep(2)

@when('I should see the two input fields "Old Password" and "New Password"')
def step_impl(context):
    driver = get_driver_instance(context)
    oldPassword = driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="old password"]')
    time.sleep(2)
    newPassword = driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="new password"]')
    time.sleep(2)
    assert oldPassword.is_displayed()
    assert newPassword.is_displayed()
    time.sleep(2)

@then('I click on the "Old Password Field" and then I entered Old Password : "{oldPassword}"')
def step_impl(context,oldPassword):
    driver = get_driver_instance(context)
    oldPasswordField = driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="old password"]')
    oldPasswordField.click()
    oldPasswordField.clear()
    oldPasswordField.send_keys(oldPassword)
    time.sleep(2)

@then('I click on the "New Password Field" and then I entered New Password : "{newPassword}"')
def step_impl(context,newPassword):
    driver = get_driver_instance(context)
    newPasswordField = driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="new password"]')
    newPasswordField.click()
    newPasswordField.clear()
    newPasswordField.send_keys(newPassword)
    time.sleep(2)

@when('I should see the Submit Button')
def step_impl(context):
    driver = get_driver_instance(context)
    submit = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'on_tap\nSubmit')
    assert submit.is_displayed()
    time.sleep(2)

@then('I click on that Submit Button')
def step_impl(context):
    driver = get_driver_instance(context)
    submit = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'on_tap\nSubmit')
    submit.click()
    time.sleep(2)

@then('I am on the Dashboard')
def step_impl(context):
    driver = get_driver_instance(context)
    submit = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Dashboard')
    assert submit.is_displayed()
    time.sleep(2)


@then('I should see the menu option and click menu')
def step_impl(context):
    driver = get_driver_instance(context)
    menu = driver.find_element(AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.ImageView[4]')
    assert menu.is_displayed()
    time.sleep(2)
    menu.click()
    time.sleep(2)

@then('I click on the "Old Password Field" and then I entered wrong Old Password : "{wrongPassword}"')
def step_impl(context,wrongPassword):
    driver = get_driver_instance(context)
    oldPasswordField = driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="old password"]')
    oldPasswordField.click()
    oldPasswordField.clear()
    oldPasswordField.send_keys(wrongPassword)
    time.sleep(2)
