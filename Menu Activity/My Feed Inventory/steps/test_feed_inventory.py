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

@when('I should see "My Feed Inventory" button')
def step_impl(context):
    driver = get_driver_instance(context)
    feed_inventory_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'My Feed Inventory')
    assert feed_inventory_button.is_displayed()
    time.sleep(2)

@then('I click "My Feed Inventory" button')
def step_impl(context):
    driver = get_driver_instance(context)
    feed_inventory_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'My Feed Inventory')
    feed_inventory_button.click()
    time.sleep(2)

@given('I am on "My Feed Inventory" Page')
def step_impl(context):
    driver = get_driver_instance(context)
    feed_inventory_page = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'My Feed Inventory')
    assert feed_inventory_page.is_displayed()
    time.sleep(2)

@when('I should see "Alfalfa" Feed in my List')
def step_impl(context):
    driver = get_driver_instance(context)
    alfalfa_feed = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Fodder\nAlfalfa\nCurrent  Stock\n400.00 kg\nCurrent Usage Weekly\n0.00 kg\n$/Kg :- 20.00')
    assert alfalfa_feed.is_displayed()
    time.sleep(2)

@then('I should see "Add New Product" button')
def step_impl(context):
    driver = get_driver_instance(context)
    add_product_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'on_tap\nAdd New Product')
    assert add_product_button.is_displayed()
    time.sleep(2)

@then('I should see Product Preview Button on "Alfalfa Feed"')
def step_impl(context):
    driver = get_driver_instance(context)
    preview_button = driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Fodder Alfalfa Current  Stock 400.00 kg Current Usage Weekly 0.00 kg $/Kg :- 20.00"]/android.view.View[1]')
    assert preview_button.is_displayed()
    time.sleep(2)

@then('I should see "Update" Button')
def step_impl(context):
    driver = get_driver_instance(context)
    update_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'on_tap\nUpdate')
    assert update_button.is_displayed()
    time.sleep(2)

@when('I should see "Update" Button of any Particular Object')
def step_impl(context):
    driver = get_driver_instance(context)
    update_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'on_tap\nUpdate')
    assert update_button.is_displayed()
    time.sleep(2)

@then('I click "Update" Button')
def step_impl(context):
    driver = get_driver_instance(context)
    update_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'on_tap\nUpdate')
    update_button.click()
    time.sleep(2)

@then('I see Update Popup is Open')
def step_impl(context):
    driver = get_driver_instance(context)
    update_popup = driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View')
    assert update_popup.is_displayed()
    time.sleep(2)


# When I should see "Supplier Name","Weight","Purchase Cost" and "Update Inventory" Button
@when('I should see "Supplier Name","Weight","Purchase Cost" and "Update Inventory" Button')
def step_impl(context):
    driver = get_driver_instance(context)
    supplier_name_field = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="Supplier"]')
    weight_field = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="weight‪(kg)"]')
    purchase_cost_field = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="purchase cost"]')
    update_inventory_button = driver.find_element(AppiumBy.XPATH, '//android.view.View[@content-desc="on_tap Update inventory"]')
    
    assert supplier_name_field.is_displayed()
    assert weight_field.is_displayed()
    assert purchase_cost_field.is_displayed()
    assert update_inventory_button.is_displayed()
    time.sleep(2)

@then('I click on "Weight" field and Enter Update value "{weight}"')
def step_impl(context,weight):
    driver = get_driver_instance(context)
    weight_field = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="weight‪(kg)"]')
    weight_field.click()
    weight_field.clear().send_keys(weight)
    time.sleep(2)

@then('I click on "Purchase Cost" and Enter Update value "{cost}"')
def step_impl(context,cost):
    driver = get_driver_instance(context)
    purchase_cost_field = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="purchase cost"]')
    purchase_cost_field.click()
    purchase_cost_field.clear().send_keys(cost)
    time.sleep(2)

@then('I click "Update Inventory" button')
def step_impl(context):
    driver = get_driver_instance(context)
    update_inventory_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'on_tap\nUpdate inventory')
    update_inventory_button.click()
    time.sleep(2)

@when('I click "Add New Product" button')
def step_impl(context):
    driver = get_driver_instance(context)
    add_product_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'on_tap\nAdd New Product')
    add_product_button.click()
    time.sleep(2)

@then('I should see "Add New Product" Popup')
def step_impl(context):
    driver = get_driver_instance(context)
    add_product_popup = driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[2]/android.view.View/android.view.View')
    assert add_product_popup.is_displayed()
    time.sleep(2)

# When I should see "Product Type","Find Product","Supplier","Weight","Purchase Cost"
@when('I should see "Product Type","Find Product","Supplier","Weight","Purchase Cost"')
def step_impl(context):
    driver = get_driver_instance(context)
    product_type_field = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Product Type')
    find_product_field = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Find Product')
    supplier_field = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Supplier')
    weight_field = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Weight')
    purchase_cost_field = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Purchase Cost')

    assert product_type_field.is_displayed()
    assert find_product_field.is_displayed()
    assert supplier_field.is_displayed()
    assert weight_field.is_displayed()
    assert purchase_cost_field.is_displayed()
    time.sleep(2)

@then('I click "Product Type" and Select "Fodder"')
def step_impl(context):
    driver = get_driver_instance(context)
    product_type_field = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="Product Type"]')
    product_type_field.click()
    fodder_option = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Fodder')
    fodder_option.click()
    time.sleep(2)

@then('I click "Find Product" and Select "Alfalfa"')
def step_impl(context):
    driver = get_driver_instance(context)
    find_product_field = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="find product"]')
    find_product_field.click()
    alfalfa_option = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Alfalfa')
    alfalfa_option.click()
    time.sleep(2)

@then('I click "Supplier" and Select "Aidco"')
def step_impl(context):
    driver = get_driver_instance(context)
    supplier_field = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="Supplier"]')
    supplier_field.click()
    aidco_option = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Aidco')
    aidco_option.click()
    time.sleep(2)

@then('I click "Weight" and Enter Weight as "{weight}"')
def step_impl(context,weight):
    driver = get_driver_instance(context)
    weight_field = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="weight‪(kg)"]')
    weight_field.click()
    weight_field.send_keys(weight)
    time.sleep(2)

@then('I click "Purchase Cost" and Enter Cost as "{cost}"')
def step_impl(context,cost):
    driver = get_driver_instance(context)
    purchase_cost_field = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="purchase cost"]')
    purchase_cost_field.click()
    purchase_cost_field.send_keys(cost)
    time.sleep(2)

@then('I click "Add to Feed" button')
def step_impl(context):
    driver = get_driver_instance(context)
    add_to_feed_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'on_tap\nAdd to Feed')
    add_to_feed_button.click()
    time.sleep(2)

