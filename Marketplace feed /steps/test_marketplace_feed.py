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
    assert driver.find_element(AppiumBy.XPATH,'//android.widget.ScrollView/android.view.View').is_displayed(),'Filter Button not display'
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
    

@then('I should see the Corn - raw Product')
def step_impl(context):
    driver = get_driver_instance(context)
    search_bar = driver.find_element(AppiumBy.XPATH,'//android.widget.EditText')
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Corn - Raw\n$ 0.37\n1.00 kg').is_displayed()
    time.sleep(2)
    search_bar.clear()
    driver.hide_keyboard()
    time.sleep(2)

@given('I am on the "Marketplace Feeds" activity')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Marketplace Feeds').is_displayed()
    time.sleep(2)

@when('I should see the "Filter" button')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.XPATH,'//android.widget.ScrollView/android.view.View').is_displayed()
    time.sleep(2)

@then('I click on the "Filter" button')
def step_impl(context):
    driver = get_driver_instance(context)
    filter_btn =  driver.find_element(AppiumBy.XPATH,'//android.widget.ScrollView/android.view.View')
    time.sleep(2)
    filter_btn.click()
    time.sleep(5)

@then('I should see the filter pop-up screen')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.XPATH,'//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View[2]/android.view.View').is_displayed()
    time.sleep(2)

@when('I select "Product Type" as "fodder" and "Animal Species" as "Cattle"')
def step_impl(context):
    driver = get_driver_instance(context)
    option1 = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'fodder')
    option2 = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Cattle')
    option1.click()
    time.sleep(2)
    option2.click()
    time.sleep(2)

@then('I should see the "Apply Filter" button')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID,'on_tap\nApply Filters').is_displayed()
    time.sleep(2)

@when('I click on the "Apply Filter" button')
def step_impl(context):
    driver = get_driver_instance(context)
    element =  driver.find_element(AppiumBy.ACCESSIBILITY_ID,'on_tap\nApply Filters')
    element.click()
    time.sleep(5)

@then('I should see a first product named as Alfa Alfa')
def step_impl(context):
    driver = get_driver_instance(context)
    element =  driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Alfa Alfa\n$ 0.39\n1.00 kg')
    time.sleep(2)
    assert element.is_displayed()
    time.sleep(2)

@when('I should see the "Remove Filters" button')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID,'on_tap\nRemove Filters').is_displayed()
    time.sleep(2)

@then('I click on the "Remove Filters" button')
def step_impl(context):
    driver = get_driver_instance(context)
    remove_btn =  driver.find_element(AppiumBy.ACCESSIBILITY_ID,'on_tap\nRemove Filters')
    remove_btn.click()
    time.sleep(2)

@then('I should see the first item as "500kg beef"')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID,'500 kg Beef Calf Mix\nVolume Discounts  Available \n$ 0.37\n1.00 kg').is_displayed()
    driver.hide_keyboard()
    time.sleep(2)

@when('I should see the first product in the product list')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID,'500 kg Beef Calf Mix\nVolume Discounts  Available \n$ 0.37\n1.00 kg').is_displayed()
    time.sleep(2)

@then('I click on the first product')
def step_impl(context):
    driver = get_driver_instance(context)
    element =  driver.find_element(AppiumBy.ACCESSIBILITY_ID,'500 kg Beef Calf Mix\nVolume Discounts  Available \n$ 0.37\n1.00 kg')
    element.click()
    time.sleep(2)

@then('I will be redirected to the "View Product Detail" page')
def step_impl(context):
    driver = get_driver_instance(context)
    element =  driver.find_element(AppiumBy.ACCESSIBILITY_ID,'View Product Details')
    assert element.is_displayed()
    time.sleep(2)

@when('I see the detail of "500 kg Beef Calf Mix"')
def step_impl(context):
    driver = get_driver_instance(context)
    element =  driver.find_element(AppiumBy.ACCESSIBILITY_ID,'500 kg Beef Calf Mix')
    assert element.is_displayed()
    time.sleep(2)

@then('I should see the price of that product')
def step_impl(context):
    driver = get_driver_instance(context)
    element =  driver.find_element(AppiumBy.ACCESSIBILITY_ID,'$ 0.37')
    assert element.is_displayed()
    time.sleep(2)

@when('I should see the "Nutritional Composition" section')
def step_impl(context):
    driver = get_driver_instance(context)
    element =  driver.find_element(AppiumBy.ACCESSIBILITY_ID,'nutritional_expanded\nNutritional Composition (per kg)')
    assert element.is_displayed()
    time.sleep(2)

@then('I should see the following items in the nutritional section:')
def step_impl(context):
    driver = get_driver_instance(context)
    items_id = [
        '//android.view.View[@content-desc="Crude Protein : "]',
        '//android.view.View[@content-desc="Fiber : "]',
        '//android.view.View[@content-desc="Fat : "]',
        '//android.view.View[@content-desc="Calcium : "]',
        '//android.view.View[@content-desc="Phosphorus : "]',
        '//android.view.View[@content-desc="Total Digestible Nutrients : "]',
        '//android.view.View[@content-desc="Moisture : "]'

        # "Fiber : ","Fat : ","Calcium : ","Phosphorus : ","Total Digestible Nutrients : ","Moisture : "
    ]

    for item_id in items_id:
        element = driver.find_element(AppiumBy.XPATH,item_id)
        assert element.is_displayed()
        time.sleep(3)
    
    time.sleep(2)

@when('I should see the "Supplier Details" section')
def step_impl(context):
    driver = get_driver_instance(context)
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"supplierDetails_expanded\nSupplier Details")
    assert element.is_displayed()
    time.sleep(2)


    def scroll_down():
        driver.execute_script("mobile: scrollGesture", {
            "left": 100, "top": 100, "width": 200, "height": 1200,
            "direction": "down",
            "percent": 1.0
        })
    
    scroll_down()
    time.sleep(2)

@then('I should see the following items in the supplier section:')
def step_impl(context):
    driver = get_driver_instance(context)
    items_id = [
        "Supplier Name","Phone Number","Address","Email"
    ]

    for item_id in items_id:
        element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,item_id)
        assert element.is_displayed()
        time.sleep(3)
    
    time.sleep(2)

@when('I should see the "Feeding Instructions" section')
def step_impl(context):
    driver = get_driver_instance(context)
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'feedingInstructions_expanded\nFeeding Instructions')
    assert element.is_displayed()
    time.sleep(2)

@then('I should see the back button on the top left side')
def step_impl(context):
    driver = get_driver_instance(context)
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'on_tap_View Product Details_back')
    assert element.is_displayed()
    time.sleep(2)

@when('I click on the back button')
def step_impl(context):
    driver = get_driver_instance(context)
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'on_tap_View Product Details_back')
    element.click()
    time.sleep(2)

@then('I should be redirected back to the "Marketplace Feeds" activity')
def step_impl(context):
    driver = get_driver_instance(context)
    driver.hide_keyboard()
    element = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Marketplace Feeds')
    assert element.is_displayed()
    time.sleep(2)








#       | Crud Protien   |
#       | Fiber          |
#       | Fat            |
#       | Calcium        |
#       | Phosphorous    |
#       | Total Dignosis |
#       | Moisture       |


#       |Supplier Name |
#       |Email         |
#       |Phone Number  |
#       |Address       |
    
