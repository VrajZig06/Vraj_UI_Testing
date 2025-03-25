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

@then('I should see and verify that all options are clickable the following options:')
def step_impl(context):
    driver = get_driver_instance(context)
    options = [
        {"type" : "id","value": "My Profile"},
        {"type" : "id","value": "Reset Password"},
        {"type" : "id","value": "Record Animal Sale"},
        {"type" : "id","value": "Onboard Groups"},
        {"type" : "id","value": "Add New Animals"},
        {"type" : "id","value": "My Feed Inventory"}, 
        {"type" : "id","value": "Animal Groups"},
        {"type" : "id","value": "Reports"},
        {"type" : "id","value": "Notifications"}, 
        {"type" : "id","value": "Help & Support"},
        {"type" : "id","value": "Logout"},
    ]

    for option in options:
        if(option['type'] == 'id'):
            assert driver.find_element(AppiumBy.ACCESSIBILITY_ID,option['value']).is_displayed()
    
        if(option['type'] == 'xpath'):
            assert driver.find_element(AppiumBy.XPATH,option['value']).is_displayed()
    time.sleep(2)    

@when('I should see the Notification button')
def step_impl(context):
    driver = get_driver_instance(context)
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'on_tap_edit')
    assert element.is_displayed()
    time.sleep(2)

@when('I see the My Profile button')
def step_impl(context):
    driver = get_driver_instance(context)
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'My Profile')
    assert element.is_displayed()
    time.sleep(2)

@then('I click on the My Profile button')
def step_impl(context):
    driver = get_driver_instance(context)
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'My Profile')
    element.click()
    time.sleep(2)

@when('I am on the My Profile page')
def step_impl(context):
    driver = get_driver_instance(context)
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'My Profile')
    element.click()
    time.sleep(2)

@then("I should see my name displayed on the Profile page")
def step_impl(context):
    driver = get_driver_instance(context)
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Zaher, ')
    assert element.is_displayed()
    time.sleep(2)

@given('I am on the My Profile page')
def step_impl(context):
    driver = get_driver_instance(context)
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'My Profile')
    element.click()
    time.sleep(2)

@when('I see the "Complete Profile Now" button')
def step_impl(context):
    driver = get_driver_instance(context)
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'on_tap\nComplete Profile Now')
    assert element.is_displayed()
    time.sleep(2)

@then('I click on the "Complete My Profile" button')
def step_impl(context):
    driver = get_driver_instance(context)
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'on_tap\nComplete Profile Now')
    element.click()
    time.sleep(2)

@then('I am redirected to the Edit My Profile Page')
def step_impl(context):
    driver = get_driver_instance(context)
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Edit My Profile')
    assert element.is_displayed()
    time.sleep(2)

@given('I am on the Edit My Profile page')
def step_impl(context):
    driver = get_driver_instance(context)
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Edit My Profile')
    assert element.is_displayed()
    time.sleep(2)

@when('I see the Full Name field and change name to {name}')
def step_impl(context,name):
    driver = get_driver_instance(context)

    element0 = driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="Preferred Language"]')
    element0.click()
    time.sleep(2)

    element1 = driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="English"]')
    element1.click()
    time.sleep(2)

    element = driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="first name"]')
    time.sleep(2)
    element.click()
    time.sleep(2)
    element.clear()
    element.send_keys(name)
    time.sleep(2)
    def scroll_down():
        driver.execute_script("mobile: scrollGesture", {
            "left": 100, "top": 100, "width": 200, "height": 1200,
            "direction": "down",
            "percent": 3.0
        })
    scroll_down()
    time.sleep(2)


@then('I click Save Button')
def step_impl(context):
    driver = get_driver_instance(context)
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'on_tap\nSave')
    element.click()
    time.sleep(2)



@then('I should see the Personal Details section')
def step_impl(context):
    driver = get_driver_instance(context)
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'My Profile')
    assert element.is_displayed()
    time.sleep(2)

@then('I should see the Farm Details and Farm Contact Numbers sections')
def step_impl(context):
    driver = get_driver_instance(context)
    element1 = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Farm Details')
    assert element1.is_displayed()
    time.sleep(2)
    element2 = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Farm contact number')
    assert element2.is_displayed()
    def scroll_down():
        driver.execute_script("mobile: scrollGesture", {
            "left": 100, "top": 100, "width": 200, "height": 1200,
            "direction": "down",
            "percent": 3.0
        })
    scroll_down()
    time.sleep(2)



@then('I should see the Delete Account and Manage Subscriptions buttons')
def step_impl(context):
    driver = get_driver_instance(context)
    element1 = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'on_tap\nDelete Account')
    assert element1.is_displayed()
    time.sleep(2)
    element2 = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'on_tap\nManage subscription')
    assert element2.is_displayed()
    time.sleep(2)   




    #   | My Profile        |
    #   | Reset Password    |
    #   | Record Animal Sale|
    #   | Add New Animal    |
    #   | My Feed Inventory |
    #   | Animal Group      |
    #   | Reports           |
    #   | Notifications     |
    #   | Help & Support    |
    #   | Logout            |