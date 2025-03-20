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

@given("I am on the Farm Dashboard page")
def step_impl(context):
    time.sleep(5)
    driver = get_driver_instance(context)
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Dashboard')
    assert element.is_displayed() ,"Dashboard is not visible or not loading properly"
    time.sleep(2)

@when("I see the group of animals displayed in different species")
def step_impl(context):
    driver = get_driver_instance(context)
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Cattle(1)')
    assert element.is_displayed(),"Animal Groups Tabs not visible"
    time.sleep(2)

@then("I should see the Animal Tag Number search bar")
def step_impl(context):
    driver = get_driver_instance(context)
    search_bar = driver.find_element(AppiumBy.XPATH,"//android.widget.EditText")
    assert search_bar.is_displayed(),"Animal search using tag Number is not visisble"
    time.sleep(2)

@then('I should see "My Herd" section')
def step_impl(context):
    driver = get_driver_instance(context)
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Your Herd')
    assert element.is_displayed()   
    time.sleep(2)

@then('I should see the status overview section')
def step_impl(context):
    driver = get_driver_instance(context)
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Status Overview')
    assert element.is_displayed()   
    time.sleep(2)

@then('I should see the AVG FCR (Average Feed Conversion Ratio) displayed')
def step_impl(context):
    driver = get_driver_instance(context)
    
    time.sleep(2)
    scroll_down(driver)

    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Avg FCR')
    assert element.is_displayed()   
    time.sleep(2)

@then('I should see the Average Daily Gain section')
def step_impl(context):
    driver = get_driver_instance(context)
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Average Daily Gain')
    assert element.is_displayed()   
    time.sleep(2)

@then('I should see the Average Calf Weight section')
def step_impl(context):
    driver = get_driver_instance(context)
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Average Calf Weight')
    assert element.is_displayed()   
    time.sleep(2)

@then('I should see the Emission overview section')
def step_impl(context):
    driver = get_driver_instance(context)
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Emissions Overview')
    assert element.is_displayed() 
    scroll_down(driver) 
    time.sleep(2) 

@then('I should see the Feed overview section')
def step_impl(context):
    driver = get_driver_instance(context)
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Feed Overview')
    assert element.is_displayed() 
    scroll_down(driver) 
    time.sleep(2)  

@then('I should see the Weather Forecast section')
def step_impl(context):
    driver = get_driver_instance(context)
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Weather Forecast')
    assert element.is_displayed()  

    # Check Current Day Name show or not 
    # today = datetime.datetime.now()
    # day_name_short = today.strftime("%a")
    
    time.sleep(2) 

@then('I should also see the Notification button')
def step_impl(context):
    driver = get_driver_instance(context)
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'on_tap_edit')
    assert element.is_displayed()  
    time.sleep(2) 

@then("I Should also see then Dashboard Button")
def step_impl(context):
    driver = get_driver_instance(context)
    element = driver.find_element(AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.widget.ImageView')
    assert element.is_displayed()  
    time.sleep(2) 
    element.click()
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Dashboard')
    time.sleep(2)