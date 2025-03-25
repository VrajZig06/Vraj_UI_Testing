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

@when('I should see "Help & Support" button')
def step_impl(context):
    driver = get_driver_instance(context)
    menuPage = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Help & Support')
    assert menuPage.is_displayed()
    time.sleep(2)


@then('I click "Help & Support" button')
def step_impl(context):
    driver = get_driver_instance(context)
    menuPage = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Help & Support')
    menuPage.click()
    time.sleep(2)

@given('I am on "Help & Support" Page')
def step_impl(context):
    driver = get_driver_instance(context)
    help_support_page = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'support@greenerherd.com')
    assert help_support_page.is_displayed()
    time.sleep(2)

@when('I should see "Select Category" Field')
def step_impl(context):
    driver = get_driver_instance(context)
    select_category_field = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="Select category"]')
    assert select_category_field.is_displayed()
    time.sleep(2)

@then('I click "Select Category" options and Select "Technical Issue"')
def step_impl(context):
    driver = get_driver_instance(context)
    select_category_field = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="Select category"]')
    select_category_field.click()
    technical_issue_option = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Technical Issue')
    technical_issue_option.click()
    time.sleep(2)

@when('I should see "Query" Field')
def step_impl(context):
    driver = get_driver_instance(context)
    query_field = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="query"]')
    assert query_field.is_displayed()
    time.sleep(2)

@then('I click and enter Query details "{Query}"')
def step_impl(context,Query):
    driver = get_driver_instance(context)
    query_field = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="query"]')
    query_field.click()
    query_field.send_keys(Query)
    driver.hide_keyboard()
    time.sleep(5)

@when('I should see "Details" Field')
def step_impl(context):
    driver = get_driver_instance(context)
    details_field = driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]')
    assert details_field.is_displayed()
    time.sleep(2)

@then('I click and enter details "{details}"')
def step_impl(context,details):
    driver = get_driver_instance(context)
    details_field = driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[2]/android.widget.EditText[2]')
    details_field.click()
    details_field.send_keys(details)
    time.sleep(2)

@when('I should see "Submit" Field')
def step_impl(context):
    driver = get_driver_instance(context)
    submit_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'on_tap\nSubmit')
    assert submit_button.is_displayed()
    time.sleep(2)

@then('I click "Submit" button')
def step_impl(context):
    driver = get_driver_instance(context)
    submit_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'on_tap\nSubmit')
    submit_button.click()
    time.sleep(2)

@then('I redirected to "Dashboard" Page')
def step_impl(context):
    driver = get_driver_instance(context)
    dashboard_page = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Dashboard')
    assert dashboard_page.is_displayed()
    time.sleep(2)

