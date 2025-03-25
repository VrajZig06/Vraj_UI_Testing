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

@when('I see the "Onboard Group" button')
def step_impl(context):
    driver = get_driver_instance(context)
    onboard_group_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Onboard Groups')
    assert onboard_group_button.is_displayed()
    time.sleep(2)

@then('I click on the "Onboard Group" option')
def step_impl(context):
    driver = get_driver_instance(context)
    onboard_group_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Onboard Groups')
    onboard_group_button.click()
    time.sleep(2)

@when('I am redirected to the Group Onboarding page')
def step_impl(context):
    driver = get_driver_instance(context)
    group_onboarding_page = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Group Onboarding')
    assert group_onboarding_page.is_displayed()
    time.sleep(2)

@then('I should see the "Animal Groups"')
def step_impl(context):
    driver = get_driver_instance(context)
    animal_groups_section = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Animal Groups')
    assert animal_groups_section.is_displayed()
    time.sleep(2)

@when('I see the "Species" dropdown')
def step_impl(context):
    driver = get_driver_instance(context)
    species_dropdown = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="Species"]')
    assert species_dropdown.is_displayed()
    time.sleep(2)

@then('I click on the "Species" dropdown')
def step_impl(context):
    driver = get_driver_instance(context)
    species_dropdown = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="Species"]')
    species_dropdown.click()
    time.sleep(2)

@then('I select "Cattle" from the list')
def step_impl(context):
    driver = get_driver_instance(context)
    cattle_option = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Cattle')
    cattle_option.click()
    time.sleep(2)

@then('I click on the "Submit" button')
def step_impl(context):
    driver = get_driver_instance(context)
    submit_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'on_tap\nSubmit')
    submit_button.click()
    time.sleep(2)

@when('I am redirected to the "On-board Groups" page')
def step_impl(context):
    driver = get_driver_instance(context)
    on_board_groups_page = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'On-board Groups')
    assert on_board_groups_page.is_displayed()
    time.sleep(2)

@then('I should see the "Cattle Group" information')
def step_impl(context):
    driver = get_driver_instance(context)
    cattle_group_info = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Cattle Group Information')
    assert cattle_group_info.is_displayed()
    time.sleep(2)

@when('I see the "Group Name" field')
def step_impl(context):
    driver = get_driver_instance(context)
    group_name_field = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="group name"]')
    assert group_name_field.is_displayed()
    time.sleep(2)

@then('I click on the "Group Name" field and enter "{groupName}"')
def step_impl(context,groupName):
    driver = get_driver_instance(context)
    group_name_field = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="group name"]')
    group_name_field.click()
    group_name_field.send_keys(groupName)
    time.sleep(2)

@when('I see the "Description" field')
def step_impl(context):
    driver = get_driver_instance(context)
    description_field = driver.find_element(AppiumBy.XPATH, '//android.widget.ScrollView/android.widget.EditText[2]')
    assert description_field.is_displayed()
    time.sleep(2)

@then('I click on the "Description" field and enter "{description}"')
def step_impl(context,description):
    driver = get_driver_instance(context)
    description_field = driver.find_element(AppiumBy.XPATH, '//android.widget.ScrollView/android.widget.EditText[2]')
    description_field.click()
    description_field.send_keys(description)
    time.sleep(2)

@when('I see the "Group Focus" field')
def step_impl(context):
    driver = get_driver_instance(context)
    group_focus_field = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="Group Focus"]')
    assert group_focus_field.is_displayed()
    time.sleep(2)

@then('I click on the "Group Focus" field and select "General" as the purpose')
def step_impl(context):
    driver = get_driver_instance(context)
    group_focus_field = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="Group Focus"]')
    group_focus_field.click()
    general_option = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'General')
    general_option.click()
    time.sleep(2)

@when('I see the "Production Focus" field')
def step_impl(context):
    driver = get_driver_instance(context)
    production_focus_field = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="Production Focus"]')
    assert production_focus_field.is_displayed()
    time.sleep(2)

@then('I click on the "Production Focus" field and select "Dairy"')
def step_impl(context):
    driver = get_driver_instance(context)
    production_focus_field = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="Production Focus"]')
    production_focus_field.click()
    dairy_option = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Dairy')
    dairy_option.click()
    time.sleep(2)

@when('I see the "Breed" field')
def step_impl(context):
    driver = get_driver_instance(context)
    breed_field = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Breed')
    assert breed_field.is_displayed()
    time.sleep(2)

@then('I select "Angus" from the breed list and click "Ok"')
def step_impl(context):
    driver = get_driver_instance(context)
    breed_field = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Breed')
    breed_field.click()
    angus_option = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Angus')
    angus_option.click()
    ok_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Ok')
    ok_button.click()
    time.sleep(2)

@then('I click on the "Next" button')
def step_impl(context):
    driver = get_driver_instance(context)
    next_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'on_tap\nNext')
    next_button.click()
    time.sleep(2)


# Phase 2: Onboard Groups Process

@given('I am on the Age Split page')
def step_impl(context):
    driver = get_driver_instance(context)
    # Ensure that the Age Split page is loaded
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Group: Age Split').is_displayed()
    time.sleep(2)

# Age range Field Locator Not Found
@when('I see the "Age Range" field')
def step_impl(context):
    driver = get_driver_instance(context)
    age_range_field = driver.find_element(AppiumBy.XPATH, '//android.view.View[@content-desc="Breed Angus Age Range"]')
    assert age_range_field.is_displayed()
    time.sleep(2)

@then('I click on the "Age Range" field and select "<2M" and click "Ok"')
def step_impl(context):
    driver = get_driver_instance(context)
    age_range_field = driver.find_element(AppiumBy.XPATH, '//android.view.View[@content-desc="Breed Angus Age Range"]')
    age_range_field.click()
    age_range_option = driver.find_element(AppiumBy.ACCESSIBILITY_ID, '<2M')
    age_range_option.click()
    ok_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Ok')
    ok_button.click()
    time.sleep(2)


# Phase 3: Onboard Groups Process

@given('I am on the Sex Split page')
def step_impl(context):
    driver = get_driver_instance(context)
    # Ensure that the Age Split page is loaded
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Group: Sex Split').is_displayed()
    time.sleep(2)


# Sex Field Locator Not Found
@when('I see the "Sex" field')
def step_impl(context):
    driver = get_driver_instance(context)
    sex_field = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Breed\nBaladi\nAge Range\n<2M\nSex')
    assert sex_field.is_displayed()
    time.sleep(2)

@then('I click on the "Sex" field and select "Female" and click "Ok"')
def step_impl(context):
    driver = get_driver_instance(context)
    sex_field = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Breed\nBaladi\nAge Range\n<2M\nSex')
    sex_field.click()
    female_option = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Female')
    female_option.click()
    ok_button = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Ok')
    ok_button.click()
    time.sleep(2)


# Phase 4: Onboard Groups Process

@given('I am on the Number of Animals page')
def step_impl(context):
    driver = get_driver_instance(context)
    sex_field = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'What is the numbers of each?')
    assert sex_field.is_displayed()
    time.sleep(2)

# Number of Animals Field Locator Not Found
@when('I see the "Number of Animals" field')
def step_impl(context):
    driver = get_driver_instance(context)
    number_of_animals_field = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="number of animals"]')
    assert number_of_animals_field.is_displayed()
    time.sleep(2)

@then('I click on the "Number of Animals" field and enter "{count}"')
def step_impl(context,count):
    driver = get_driver_instance(context)
    number_of_animals_field = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@resource-id="number of animals"]')
    number_of_animals_field.click()
    number_of_animals_field.send_keys(count)
    time.sleep(2)

# Phase 5: Onboard Groups Process

@given('I am on the Group Summary page')
def step_impl(context):
    driver = get_driver_instance(context)
    sex_field = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Group Summary')
    assert sex_field.is_displayed()
    time.sleep(2)


@when('I see the "Group Overview"')
def step_impl(context):
    driver = get_driver_instance(context)
    group_overview = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Group Overview')
    assert group_overview.is_displayed()

    def scroll_down(driver):
        driver.execute_script("mobile: scrollGesture", {
            "left": 100, "top": 100, "width": 200, "height": 1200,
            "direction": "down",
            "percent": 4.0
        })

    scroll_down()

    time.sleep(2)



@then('I am on the Menu page')
def step_impl(context):
    driver = get_driver_instance(context)
    menu_page = driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Menu Page')
    assert menu_page.is_displayed()
    time.sleep(2)

