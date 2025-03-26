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

@when('I should see "Add New Animal" option')
def step_impl(context):
    driver = get_driver_instance(context)
    menuPage = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Add New Animals')
    assert menuPage.is_displayed()
    time.sleep(2)


@then('I click on "Add Animal Record" option')
def step_impl(context):
    driver = get_driver_instance(context)
    menuPage = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Add New Animals')
    menuPage.click()
    time.sleep(2)

@given('I am on the Add Animal Record Page')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Add Animal Record').is_displayed()
    time.sleep(2)
    
@when('I should see Purchase Information')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Purchase Information').is_displayed()
    time.sleep(2)

@then('I should see two Dropdown box "Add Animal Species" and "Add Animal Source"')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="Add Animal species"]').is_displayed()
    assert driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="Add animal source"]').is_displayed()
    time.sleep(2)

@then('I click on "Add Animal Species" and select "Cattle" as Species')
def step_impl(context):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="Add Animal species"]').click()
    time.sleep(2)
    option = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Cattle')
    option.click()
    time.sleep(2)

@then('I click on "Add Animal Source" and select "Purchased" as Animal Source')
def step_impl(context):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="Add animal source"]').click()
    time.sleep(2)
    option = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Purchased')
    option.click()
    time.sleep(4)   

@then('I click on "Next" button')
def step_impl(context):
    driver = get_driver_instance(context)
    nextBtn = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'on_tap\nNext')
    nextBtn.click()
    time.sleep(3)



@given('I am on Purchase Information Page')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Purchase Information').is_displayed()
    time.sleep(3)

@when('I should see Following Fields')
def step_impl(context):
    driver = get_driver_instance(context)

    xpaths = [
        '//android.widget.EditText[@resource-id="seller name"]',
        '//android.widget.EditText[@resource-id="price paid ‪($)"]',
        '//android.widget.EditText[@resource-id="combined weight ‪(kg)"]',
        '//android.widget.EditText[@resource-id="number of animals"]',
        '//android.widget.Button[@resource-id="Production Focus"]'
    ]

    for xpath in xpaths:
        assert driver.find_element(AppiumBy.XPATH,xpath).is_displayed()
        time.sleep(1)

    time.sleep(2)

@then('I click "Seller Name" Field and enter seller name "{sname}"')
def step_impl(context,sname):
    driver = get_driver_instance(context)
    input = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="seller name"]')
    input.click()
    time.sleep(1)
    input.send_keys(sname)
    time.sleep(2)

@then('I click "Price Paid" Field and enter price paid value "{price}"')
def step_impl(context,price):
    driver = get_driver_instance(context)
    input = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="price paid ‪($)"]')
    input.click()
    time.sleep(1)
    input.send_keys(price)
    time.sleep(2)

@then('I click "Combined Weight" and enter weight "{weight}"')
def step_impl(context,weight):
    driver = get_driver_instance(context)
    input = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="combined weight ‪(kg)"]')
    input.click()
    time.sleep(1)
    input.send_keys(weight)
    time.sleep(2)

@then('I click "Number of Animals" and enter animal count as "{animalCount}"')
def step_impl(context,animalCount):
    driver = get_driver_instance(context)
    input = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="number of animals"]')
    input.click()
    time.sleep(1)
    input.send_keys(animalCount)
    time.sleep(2)

@then('I click "Production Focus" and select "Dairy"')
def step_impl(context):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="Production Focus"]').click()
    time.sleep(1)
    option = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Dairy')
    option.click()
    time.sleep(2)

@then('I click "select date of Purchase" and click on "Ok" button')
def step_impl(context):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="date purchased"]').click()
    time.sleep(1)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'on_tap\nOk').click()
    time.sleep(2)


@given('I am on "Animal Information" Page')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Add Animal Record').is_displayed()
    time.sleep(2)

@when('I should see "Add Animal Photo" Field')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'on_tap_farm_photo\nAdd animal photo\nAnimal Photo').is_displayed()
    time.sleep(2)

@then('I click on "Add Animal Photo" and select "Camera" option')
def step_impl(context):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'on_tap_farm_photo\nAdd animal photo\nAnimal Photo').click()    
    time.sleep(1)
    option = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Camera')
    option.click()
    time.sleep(2)

@when('I should be on the Camera Module of my Phone')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.XPATH,'//android.view.View[@resource-id="com.oplus.camera:id/face_view"]').is_displayed()
    time.sleep(3)

@then('I click on "Shutter" button and then I click on "Correct" option')
def step_impl(context):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, '"Shutter" button').click()
    time.sleep(5)
    driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.oplus.camera:id/done_button"]').click()
    time.sleep(2)

@when('I should see "Tag Number" Field')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="tag number"]').is_displayed()
    time.sleep(2)

@then('I click "Tag Number" Field and Enter Tag Number "{tagNumber}"')
def step_impl(context,tagNumber):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="tag number"]').click()
    time.sleep(1)
    
    driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="tag number"]').clear().send_keys(tagNumber)
    time.sleep(2)

@when('I should see "Breed" Field')
def step_impl(context):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="Breed"]')
    time.sleep(2)

@then('I click on "Breed" and select "{breed}"')
def step_impl(context,breed):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.XPATH,'//android.widget.Button[@resource-id="Breed"]').click()
    time.sleep(1)
    option = driver.find_element(AppiumBy.XPATH, f'//android.view.View[@content-desc="{breed}"]')
    option.click()
    time.sleep(2)

@when('I should see "Name" Field')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="name"]').is_displayed()
    time.sleep(2)

@then('I click on "Name" and enter "{Animalname}"')
def step_impl(context,Animalname):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="name"]').click()
    time.sleep(1)
    driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="name"]').clear().send_keys(Animalname)
    driver.hide_keyboard()
    time.sleep(2)

@when('I should see "Age" Field')
def step_impl(context):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="age"]')
    time.sleep(2)

@then('I click on "Age" and enter "{age}"')
def step_impl(context,age):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="age"]').click()
    time.sleep(1)
    driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="age"]').send_keys(age)
    time.sleep(2)
    def scroll_down():
        driver.execute_script("mobile: scrollGesture", {
            "left": 100, "top": 100, "width": 200, "height": 1200,
            "direction": "down",
            "percent": 1.0
        })
    scroll_down()
    driver.hide_keyboard()
    time.sleep(2)

@when('I should see "Sex" Field')
def step_impl(context):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="Sex"]')
    time.sleep(2)

@then('I click "Sex" and select "{Sex}"')
def step_impl(context,Sex):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="Sex"]').click()
    time.sleep(1)
    option = driver.find_element(AppiumBy.ACCESSIBILITY_ID,Sex)
    option.click()
    time.sleep(2)   

@when('I should see "Birth Weight" Field')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="birth weight kg"]').is_displayed()
    time.sleep(1)

@then('I click "Birth Weight" and enter "{weight}"')
def step_impl(context,weight):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="birth weight kg"]').click()
    time.sleep(1)
    driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="birth weight kg"]').send_keys(weight)
    time.sleep(2)

@when('I should see "Breeding Stage" Field')
def step_impl(context):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="Breeding Stage"]')
    time.sleep(2)

@then('I click "Breeding Stage" and select "{breedingStage}"')
def step_impl(context,breedingStage):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="Breeding Stage"]').click()
    time.sleep(1)
    option = driver.find_element(AppiumBy.ACCESSIBILITY_ID, breedingStage)
    option.click()
    time.sleep(2)

@when('I should see "Dam", "Sire" and "Documents" Fields')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="dam"]').is_displayed()
    assert driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="sire"]').is_displayed()
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'on_tap_farm_photo\nAdd Document\nDocuments').is_displayed()
    time.sleep(2)
    def scroll_down():
        driver.execute_script("mobile: scrollGesture", {
            "left": 0,               # Starting x-coordinate for the scroll gesture
            "top": 800,              # Starting y-coordinate (adjust based on your app's content)
            "width": 200,            # Width of the scrollable content
            "height": 1200,          # Height of the scrollable content (adjust if necessary)
            "direction": "up",       # Scroll up
            "percent": 1.0       
        })
    scroll_down()

@then('I click "date of birth" and click "Ok"')
def step_impl(context):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.XPATH, '//android.view.View[@resource-id="date of birth"]').click()
    time.sleep(1)
    option = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'on_tap\nOk')
    option.click()
    time.sleep(2)


@given('I am on "Animal Added" Page')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Animal Added').is_displayed()
    time.sleep(2)

@given('I am on "Allocate to a Group" page')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Allocate to a Group').is_displayed()
    time.sleep(2)

@when('I should see "CheckBox with my Animal"')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Allocate to a Group').get_attribute('checked') == 'false'
    time.sleep(2)

@then('I check that CheckBox')
def step_impl(context):
    driver = get_driver_instance(context)
    # driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Allocate to a Group').get_attribute('checked') == 'true'
    driver.find_element(AppiumBy.CLASS_NAME,'android.widget.CheckBox').click()
    time.sleep(2)

@given('I am on "Add to Group" Page')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="recommended group"]').is_displayed()
    time.sleep(2)

@when('I should see Two options "Recommended Group" and "Create a new Group"')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="recommended group"]').is_displayed()
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'on_tap\nCreate a new group').is_displayed()
    time.sleep(2)

@then('I click "Recommended Group" and select group "New data"')
def step_impl(context):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="recommended group"]').click()
    time.sleep(2)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'New data').click()
    time.sleep(2)   

@then('I click "Submit button"')
def step_impl(context):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'on_tap\nSubmit').click()
    time.sleep(2)

@then('I scroll')
def step_impl(context):
    driver = get_driver_instance(context)
    def scroll_down():
        driver.execute_script("mobile: scrollGesture", {
            "left": 100, "top": 100, "width": 200, "height": 1200,
            "direction": "down",
            "percent": 1.0
        })
    scroll_down()
    def scroll_down1():
        driver.execute_script("mobile: scrollGesture", {
            "left": 0,               # Starting x-coordinate for the scroll gesture
            "top": 800,              # Starting y-coordinate (adjust based on your app's content)
            "width": 200,            # Width of the scrollable content
            "height": 1200,          # Height of the scrollable content (adjust if necessary)
            "direction": "up",       # Scroll up
            "percent": 1.0       
        })
    scroll_down1()
    time.sleep(2)



