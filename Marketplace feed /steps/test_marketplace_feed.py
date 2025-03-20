from behave import given, when, then
from appium.webdriver.common.appiumby import AppiumBy
from driver import get_driver
import time

# Initialize driver
def get_driver_instance(context):
    if not hasattr(context, 'driver'):
        context.driver = get_driver()
    return context.driver

@given("I am on the Dashboard Page")
def step_impl(context):
    driver = get_driver_instance(context)
    dashboard = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Dashboard')
    assert dashboard.is_displayed(),'Dashboard Not Display'
    time.sleep(2)

@then("I should see all 5 menus displayed")
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.ImageView[1]').is_displayed(),'Group Overview not display'
    assert driver.find_element(AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.ImageView[2]').is_displayed(),'Notifications button not display'
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Dashboard').is_displayed(),'Dashboard button not display'
    assert driver.find_element(AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.ImageView[3]').is_displayed(),'Marketplace products not display'
    assert driver.find_element(AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.ImageView[4]').is_displayed(),'Menu Button not display'
    time.sleep(2)

@then("I should see the Marketplace button displayed")
def step_impl(context):
    driver = get_driver_instance(context)
    marketplace_btn = driver.find_element(AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.ImageView[3]')
    assert marketplace_btn.is_displayed(),"Marketplace button not Dispaly"
    time.sleep(2)


@when("I click on the Marketplace button")
def step_impl(context):
    driver = get_driver_instance(context)
    marketplace_btn = driver.find_element(AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.ImageView[3]')
    marketplace_btn.click()
    time.sleep(2)

@then('I should be redirected to the Marketplace Page')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Marketplace Feeds').is_displayed(),'Marketplace Product page not display properly'
    time.sleep(2)

@then("I should see the Search bar and Filter button")
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.XPATH,'//android.widget.EditText').is_displayed(),'Search Product bar is not display'
    assert driver.find_element(AppiumBy.XPATH,'//android.widget.ScrollView/android.view.View'),'Filter Button not display'
    time.sleep(2)

@then('I should see the Notification button')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID,'on_tap_edit'),'Notification button not display'
    time.sleep(2)

@then("I should see a list of products displayed")
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.XPATH,'//android.widget.ScrollView').is_displayed(),'There is no list of products'
    first_product = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'500 kg Beef Calf Mix\nVolume Discounts  Available \n$ 0.37\n1.00 kg')
    assert first_product.is_displayed(),'First Product not display'
    time.sleep(2)


@when("I Enter product name to Search bar '{product_name}'")
def step_impl(context,product_name):
    driver = get_driver_instance(context)
    search_bar = driver.find_element(AppiumBy.XPATH,'//android.widget.EditText')
    search_bar.click()
    time.sleep(2)
    assert search_bar.is_displayed(),'Search Bar is not display'
    search_bar.send_keys(product_name)
    time.sleep(2)
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Corn - Raw\n$ 0.37\n1.00 kg').is_displayed()
    time.sleep(2)
    search_bar.clear()
    time.sleep(2)


