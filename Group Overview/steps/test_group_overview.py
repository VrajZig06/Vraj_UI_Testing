from behave import given, when, then
from appium.webdriver.common.appiumby import AppiumBy
from driver import get_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize driver
def get_driver_instance(context):
    if not hasattr(context, 'driver'):
        context.driver = get_driver()
    return context.driver

def is_element_displayed(driver, locator, locator_type=AppiumBy.ACCESSIBILITY_ID, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.visibility_of_element_located((locator_type, locator))
        )
        return element.is_displayed()
    except Exception as e:
        print(f"Error: Element with locator {locator} not found or not visible. Error: {str(e)}")
        return False

def click_element(driver, locator, locator_type=AppiumBy.ACCESSIBILITY_ID, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((locator_type, locator))
        )
        element.click()
    except Exception as e:
        print(f"Error: Could not click on element with locator {locator}. Error: {str(e)}")
        raise

# Step Definitions

@given("I am on the Dashboard page")
def step_impl(context):
    driver = get_driver_instance(context)
    assert is_element_displayed(driver, 'Dashboard'), "Dashboard is not visible or not loading properly"

@then('I should see the "Group Overview" button')
def step_impl(context):
    driver = get_driver_instance(context)
    assert is_element_displayed(driver, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.ImageView[1]', locator_type=AppiumBy.XPATH)

@when('I click on the "Group Overview" button')
def step_impl(context):
    driver = get_driver_instance(context)
    click_element(driver, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.ImageView[1]', locator_type=AppiumBy.XPATH)

@then('I should be redirected to the "Group Overview" page')
def step_impl(context):
    driver = get_driver_instance(context)
    assert is_element_displayed(driver, 'Group overview')

@then('I should be able to view the group list and clickable')
def step_impl(context):
    driver = get_driver_instance(context)
    item_ids = ['hello ‪(1)', 'sdygfyxncbyacgfey ‪(0)']
    for item_id in item_ids:
        assert is_element_displayed(driver, item_id, locator_type=AppiumBy.ACCESSIBILITY_ID)

@when('I click on the first group in the group list : Group Id :- "{group_id}"')
def step_impl(context, group_id):
    driver = get_driver_instance(context)
    click_element(driver, group_id)

@then('I should be redirected to the "Group Details" page and Verify Same Group Detail : Group Id :- "{group_id}"')
def step_impl(context, group_id):
    driver = get_driver_instance(context)
    assert is_element_displayed(driver, 'Group Details')
    assert is_element_displayed(driver, group_id, locator_type=AppiumBy.ACCESSIBILITY_ID)

@then('I should see the following elements')
def step_impl(context):
    driver = get_driver_instance(context)
    elements = [
        {'by': 'id', 'value': 'on_animal_group_count\nCattle  ‪(1)'},
        {'by': 'xpath', 'value': '//android.widget.EditText'},
        {'by': 'id', 'value': 'hello  ‪(1)'},
        {'by': 'xpath', 'value': '//android.view.View[@content-desc="nanab"]'},
        {'by': 'xpath', 'value': '//android.view.View[@content-desc="General"]'},
        {'by': 'id', 'value': 'sales_expanded\nAnimals\n(1 Animals)'},
        {'by': 'id', 'value': 'Upcoming Task\n(0 tasks)'},
    ]

    def scroll_down():
        driver.execute_script("mobile: scrollGesture", {
            "left": 100, "top": 100, "width": 200, "height": 1200,
            "direction": "down",
            "percent": 1.0
        })

    for element in elements:
        if element['by'] == 'xpath':
            assert is_element_displayed(driver, element['value'], locator_type=AppiumBy.XPATH)
        elif element['by'] == 'id':
            if element['value'] == 'Upcoming Task\n(0 tasks)':
                scroll_down()
                time.sleep(2)
            assert is_element_displayed(driver, element['value'], locator_type=AppiumBy.ACCESSIBILITY_ID)

@then('I should see the "Notification" button')
def step_impl(context):
    driver = get_driver_instance(context)
    assert is_element_displayed(driver, 'on_tap_edit')
