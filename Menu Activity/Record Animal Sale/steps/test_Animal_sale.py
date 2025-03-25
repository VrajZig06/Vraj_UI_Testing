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

@when('I should see the Record Animal Sale option')
def step_impl(context):
    driver = get_driver_instance(context)
    Record_Animal_Sale = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Record Animal Sale')
    assert Record_Animal_Sale.is_displayed()
    time.sleep(2)

@then('I click on the Record Animal Sale option')
def step_impl(context):
    driver = get_driver_instance(context)
    Record_Animal_Sale = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Record Animal Sale')
    Record_Animal_Sale.click()
    time.sleep(2)

@then('I am redirect to Animal Selling Record')
def step_impl(context):
    driver = get_driver_instance(context)
    Record_Animal_Sale = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Animal Selling Record')
    assert Record_Animal_Sale.is_displayed()
    time.sleep(2)

@given('I am on the Animal Selling page')
def step_impl(context):
    driver = get_driver_instance(context)
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Animal Selling Record')
    assert element.is_displayed()
    time.sleep(2)

@when('I see the 3 stages at the top of the app')
def step_impl(context):
    driver = get_driver_instance(context)
    stage_1 = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'1')
    stage_2 = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'2')
    stage_3 = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'3')

    assert stage_1.is_displayed()
    assert stage_2.is_displayed()
    assert stage_3.is_displayed()
    time.sleep(2)

@then('I should see the Sell Information section')
def step_impl(context):
    driver = get_driver_instance(context)
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Sell Information")
    assert element.is_displayed()
    time.sleep(2)

@then('I should see the following options')
def step_impl(context):
    driver = get_driver_instance(context)

    options = [
        "Add Animal species","purchaser name","select date of sell","number of animals","price paid ‪($)","weight ‪(kg)"
    ]       

    for element_id in options:
        element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,element_id)
        assert element.is_displayed()

    time.sleep(2)

@when('I see the "Add Animal Species" option')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="Add Animal species"]').is_displayed()
    time.sleep(2)

@then('I click on the "Add Animal Species" option')
def step_impl(context):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="Add Animal species"]').click()
    time.sleep(2)

@then('I select the first option "Cattle"')
def step_impl(context):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Cattle").click()
    time.sleep(2)

@when('I see the "Purchaser Name" option')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="purchaser name"]').is_displayed()
    time.sleep(2)

@then('I click on the "Purchaser Name" option')
def step_impl(context):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="purchaser name"]').click()
    time.sleep(2)

@then('I enter the name "{name}"')
def step_impl(context,name):
    driver = get_driver_instance(context)
    purchaserName = driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="purchaser name"]')
    purchaserName.clear()
    purchaserName.send_keys(name)
    time.sleep(2)


@when('I see the "Select Date to Sell" option')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.XPATH,'//android.view.View[@resource-id="select date of sell"]').is_displayed()
    time.sleep(2)

@then('I click on the calendar button and select a date')
def step_impl(context):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.XPATH,'//android.view.View[@resource-id="select date of sell"]').click()
    time.sleep(2)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID,"on_tap\nOk").click()
    time.sleep(2)

@when('I see the "Number of Animals" option')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="number of animals"]').is_displayed()
    time.sleep(2)

@then('I click on the option and enter the number of animals "{count}"')
def step_impl(context,count):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="number of animals"]').click()
    time.sleep(2)
    driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="number of animals"]').send_keys(count)
    time.sleep(2)


@when('I see the "Price Paid" option')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="price paid ‪($)"]').is_displayed()
    time.sleep(2)

@then('I click on the "Price Paid" option and enter the price "{Price}"')
def step_impl(context,Price):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="price paid ‪($)"]').click()
    time.sleep(2)
    driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="price paid ‪($)"]').send_keys(Price)
    time.sleep(2)


@when('I see the "Weight" option')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="weight ‪(kg)"]').is_displayed()
    time.sleep(2)

@then('I click on the "Weight" option and enter the weight "{weight}"')
def step_impl(context,weight):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="weight ‪(kg)"]').click()
    time.sleep(2)
    driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="weight ‪(kg)"]').send_keys(weight)
    time.sleep(2)
    driver.hide_keyboard()
    time.sleep(2)



@then('I should be redirected to the "{stage_no}" stage of the Animal Selling Activity')
def step_impl(context,stage_no):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID,"on_tap\nNext").is_displayed()
    time.sleep(2)   

@when('I see the "Enter Animal Tag Number" option')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="Enter animal tag number"]').is_displayed()
    time.sleep(2)

@then('I click on "Enter Animal Tag Number" option')
def step_impl(context,weight):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="Enter animal tag number"]').is_displayed()
    time.sleep(2)
    driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="Enter animal tag number"]').send_keys(weight)
    time.sleep(2)

@when('I see the "Search Bar" option')
def step_impl(context,weight):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.XPATH,"//android.widget.EditText").is_displayed()
    time.sleep(2)


@then('I click on the search bar and enter the tag number "{tagNumber}"')
def step_impl(context,tagNumber):
    driver = get_driver_instance(context)
    searchBar = driver.find_element(AppiumBy.XPATH,"//android.widget.EditText")
    searchBar.click()
    time.sleep(2)
    searchBar.clear()
    time.sleep(2)
    searchBar.send_keys(tagNumber)
    time.sleep(2)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Yahooo').click()
    time.sleep(2)


@then('I Should see the details of my sale Animal Details "{tagname}"')
def step_impl(context,tagNumber):
    driver = get_driver_instance(context)   
    next = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Yahoo\nTag Number\nYahooo\nSex\nFemale\nAge (M)\n662\nWeight(kg)\nN/A")
    assert next.is_displayed()
    time.sleep(2)


@then('I redirect to the Dashboard Page')
def step_impl(context,tagNumber):
    driver = get_driver_instance(context)   
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Dashboard").is_displayed()
    time.sleep(2)


@when('I see the "Next" button')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID,"on_tap\nNext").is_displayed()
    time.sleep(2)

@when('I click Next button')
def step_impl(context):
    driver = get_driver_instance(context)
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID, "on_tap\nNext")
    element.click()
    time.sleep(5)




#  Then I should see the following options




