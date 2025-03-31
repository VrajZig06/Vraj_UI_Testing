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


# def scroll_down(driver):
#     driver.execute_script("mobile: scrollGesture", {
#         "left": 100, "top": 0, "width": 200, "height": 700,
#         "direction": "down",
#         "percent": 1.0
#     })

@given('I click on Greener Herd app')
def step_impl(context):
    driver = get_driver_instance(context)
    element = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@content-desc="Greener Herd"]')
    element.click()
    time.sleep(5)

@then('I see the splash screen')
def step_impl(context):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.XPATH, '//android.widget.ImageView')
    time.sleep(5)

@then('I see the Welcome popup')
def step_impl(context):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Welcome to\nGreener Herd')
    time.sleep(2)

@when("I Click on Continue with Email")
def step_impl(context):
    driver = get_driver_instance(context)
    continueWithPhone = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Continue with Email")
    time.sleep(2)
    continueWithPhone.click()
    time.sleep(2)

@given("I am at Login Activity")
def step_impl(context):
    driver = get_driver_instance(context)
    time.sleep(2)
    driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="Login"]')
    time.sleep(5)


@when("I Click on Email Field and I Enter my Email {email}")
def step_impl(context,email):
    driver = get_driver_instance(context)
    emailField = driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="email address"]')
    emailField.click()
    time.sleep(2)
    emailField.send_keys(email)
    time.sleep(2)
    driver.hide_keyboard()
    time.sleep(2)


@then("I click on password Field and I Enter my password {password}")
def step_impl(context,password):
    driver = get_driver_instance(context)
    passwordField = driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@resource-id="password"]')
    time.sleep(2)
    passwordField.click()
    time.sleep(2)
    passwordField.send_keys(password)
    time.sleep(2)
    driver.hide_keyboard()
    time.sleep(2)


@then("I click on Login Button")
def step_impl(context):
    driver = get_driver_instance(context)
    loginButton = driver.find_element(AppiumBy.ACCESSIBILITY_ID,"on_tap\nLogin")
    time.sleep(2)
    loginButton.click()
    time.sleep(2)

@then("I am at dashboard Page")
def step_impl(context):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID,"Dashboard")
    time.sleep(2)

@given('I am on the Dashboard Page')
def step_impl(context):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Dashboard")
    time.sleep(2)

@when('I see the "Menu" button')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.ImageView[4]')
    time.sleep(2)

@then('I click on the "Menu" button')
def step_impl(context):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View[3]/android.widget.ImageView[4]').click()
    time.sleep(2)

@then('I should be redirected to the Menu Page')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Menu").is_displayed()
    time.sleep(2)

@given('I am on the Menu Page')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Menu").is_displayed()
    time.sleep(2)

@when('I see the "My Profile" option')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID, "My Profile").is_displayed()
    time.sleep(2)

@then('I click on the "My Profile" button')
def step_impl(context):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "My Profile").click()
    time.sleep(2)

@then('I should be redirected to the My Profile Page')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID, "My Profile").is_displayed()
    time.sleep(2)

@given('I am on the My Profile Page')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID, "My Profile").is_displayed()
    time.sleep(2)
    def scroll_down():
        driver.execute_script("mobile: scrollGesture", {
            "left": 100, "top": 100, "width": 200, "height": 1200,
            "direction": "down",
            "percent": 1.0
        })

    scroll_down()
    time.sleep(2)

@when('I see the "Subscription Plan" details at the bottom of the Profile Page')
def step_impl(context):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Subscription Plan")
    time.sleep(2)

@then('I verify the subscription plan is "Trial Plan"')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.XPATH, '(//android.view.View[@content-desc="Trial Plan"])[1]').get_attribute('content-desc') == 'Trial Plan'
    # assert subscription_plan == "Trial Plan"
    time.sleep(2)

@when('I see the "Manage Subscription" button')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID, "on_tap\nManage subscription").is_displayed()
    time.sleep(2)

@then('I click on the "Manage Subscription" button')
def step_impl(context):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "on_tap\nManage subscription").click()
    time.sleep(2)

@then('I should be redirected to the Manage Subscription Page')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Manage Subscription").is_displayed()
    time.sleep(2)

@given('I am on the Manage Subscription Page')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Manage Subscription").is_displayed()
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Features").is_displayed()
    time.sleep(2)

@when('I see the "Features Description" at the top of the screen')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Designed for the realities of farming, our subscriptions offer scalable pricing that grows with your operation. Select a tier that fits your baseline, with a generous 100% amnesty buffer on capacity that ensures you're never constrained by unexpected herd growth or seasonal changes.").is_displayed()
    time.sleep(2)

@then('I verify that "Limited Offer" is displayed')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Limited Offer \nuntil the 14th of April 2025\n50% of all Annual Subscriptions").is_displayed()
    time.sleep(2)

@when('I see all available subscription plans listed below')
# def step_impl(context):
#     driver = get_driver_instance(context)


#     def scroll_down():
#         driver.execute_script("mobile: scrollGesture", {
#             "left": 100, "top": 100, "width": 200, "height": 800,
#             "direction": "down",
#             "percent": 1.0
#         })

#     subscription_plan = [
#         'Less than 25 head',
#         'Between 26 and 50 head',
#         'Between 51 and 100 head',
#         'Between 101 and 300 head',
#         'Between 301 and 1000 head'
#     ]
   
#     for i in subscription_plan:
#         assert driver.find_element(AppiumBy.ACCESSIBILITY_ID, i).is_displayed()
#         if i == 'Less than 25 head':
#             first_plan =  driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Monthly\n₹820.00\n1 Month Amnesty')
#             assert first_plan.is_displayed()
#             # first_plan.click()
#             assert driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Annual\n₹3,350.00\n₹6,700.00\n3 Month Amnesty').is_displayed()

#         elif i == 'Between 26 and 50 head':
#             assert driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Monthly\n₹1,400.00\n1 Month Amnesty').is_displayed()
#             time.sleep(1)
#             assert driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Annual\n₹5,600.00\n₹11,200.00\n3 Month Amnesty').is_displayed()

#         elif i == 'Between 51 and 100 head':
#             assert driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Monthly\n₹2,100.00\n1 Month Amnesty').is_displayed()
#             time.sleep(1)
#             assert driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Annual\n₹9,200.00\n₹18,400.00\n3 Month Amnesty').is_displayed()

#         elif i == 'Between 101 and 300 head':
#             second_plan = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Monthly\n₹4,600.00\n1 Month Amnesty')
#             assert second_plan.is_displayed()
#             second_plan.click()
#             time.sleep(1)
#             assert driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Annual\n₹22,350.00\n₹44,700.00\n3 Month Amnesty').is_displayed()

#         elif i == 'Between 301 and 1000 head':
#             assert driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Monthly\n₹10,300.00\n1 Month Amnesty').is_displayed()
#             time.sleep(1)
#             assert driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Annual\n₹42,000.00\n₹84,000.00\n3 Month Amnesty').is_displayed()

#         time.sleep(2)
#         scroll_down()   
        
        
#     time.sleep(2)
def step_impl(context):
    driver = get_driver_instance(context)


    def scroll_down():
        driver.execute_script("mobile: scrollGesture", {
            "left": 100, "top": 100, "width": 200, "height": 800,
            "direction": "down",
            "percent": 1.0
        })

    subscription_plan = [
        'Less than 25 head',
        'Between 26 and 50 head',
        'Between 51 and 100 head',
        'Between 101 and 300 head',
        'Between 301 and 1000 head'
    ]
   
    for i in subscription_plan:
        assert driver.find_element(AppiumBy.ACCESSIBILITY_ID, i).is_displayed()
        if i == 'Less than 25 head':
            first_plan =  driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Monthly\n₹820.00\n1 Month Amnesty')
            assert first_plan.is_displayed()
            # first_plan.click()
            assert driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Annual\n₹6,700.00\n3 Month Amnesty').is_displayed()

        elif i == 'Between 26 and 50 head':
            plan =  driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Monthly\n₹1,400.00\n1 Month Amnesty')
            assert plan.is_displayed()
            # plan.click()
            time.sleep(1)
            assert driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Annual\n₹11,200.00\n3 Month Amnesty').is_displayed()

        elif i == 'Between 51 and 100 head':
            assert driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Monthly\n₹2,100.00\n1 Month Amnesty').is_displayed()
            time.sleep(1)
            assert driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Annual\n₹18,400.00\n3 Month Amnesty').is_displayed()

        elif i == 'Between 101 and 300 head':
            second_plan = driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Monthly\n₹4,600.00\n1 Month Amnesty')
            assert second_plan.is_displayed()
            second_plan.click()
            time.sleep(1)
            assert driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Annual\n₹44,700.00\n3 Month Amnesty').is_displayed()

        elif i == 'Between 301 and 1000 head':
            assert driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Monthly\n₹10,300.00\n1 Month Amnesty').is_displayed()
            time.sleep(1)
            assert driver.find_element(AppiumBy.ACCESSIBILITY_ID,'Annual\n₹84,000.00\n3 Month Amnesty').is_displayed()

        time.sleep(2)
        scroll_down()   
        
        
    time.sleep(2)

@when('I verify that the "Select Plan and Subscribe" button is visible')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID, "on_tap\nPay ₹4,600.00").is_displayed()
    time.sleep(2)

@then('I click on "Pay ₹4,600.00" button')
def step_impl(context):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "on_tap\nPay ₹4,600.00").click()
    time.sleep(5)


@then('I should see PopUp Box')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Google Play").is_displayed()
    # assert driver.find_element(AppiumBy.XPATH,'(//android.widget.LinearLayout[@resource-id="com.android.vending:id/0_resource_name_obfuscated"])[7]/android.widget.LinearLayout[2]').is_displayed()
    # assert driver.find_element(AppiumBy.XPATH, '(//android.widget.LinearLayout[@resource-id="com.android.vending:id/0_resource_name_obfuscated"])[7]/android.widget.LinearLayout[3]').is_displayed()
    # assert driver.find_element(AppiumBy.XPATH,'(//android.widget.LinearLayout[@resource-id="com.android.vending:id/0_resource_name_obfuscated"])[7]/android.widget.LinearLayout[4]').is_displayed()
    time.sleep(5)

# (//android.widget.LinearLayout[@resource-id="com.android.vending:id/0_resource_name_obfuscated"])[4]/android.widget.LinearLayout -- Subscripton Done
# (//android.widget.LinearLayout[@resource-id="com.android.vending:id/0_resource_name_obfuscated"])[4]/android.widget.ImageView[2]


@when('I should see "Subscribe" button')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.android.vending:id/0_resource_name_obfuscated"]').is_displayed()
    time.sleep(5)


@then('I click on "Subscribe" button')
def step_impl(context):
    driver = get_driver_instance(context)
    driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@resource-id="com.android.vending:id/0_resource_name_obfuscated"]').click()
    time.sleep(3)

@then('I should see "Subscribed Successfull" Message')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.XPATH, '(//android.widget.LinearLayout[@resource-id="com.android.vending:id/0_resource_name_obfuscated"])[4]/android.widget.LinearLayout').is_displayed()
    assert driver.find_element(AppiumBy.XPATH, '(//android.widget.LinearLayout[@resource-id="com.android.vending:id/0_resource_name_obfuscated"])[4]/android.widget.ImageView[2]').is_displayed()
    time.sleep(2)

@given('I should see "Payment" Popup Modal')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Google Play").is_displayed()
    time.sleep(2)


@when('I should see "Payment using Card" Option')
def step_impl(context):
    driver = get_driver_instance(context)
    assert driver.find_element(AppiumBy.XPATH, '(//android.widget.LinearLayout[@resource-id="com.android.vending:id/0_resource_name_obfuscated"])[7]/android.widget.LinearLayout[2]').is_displayed()
    time.sleep(2)

@then('I click on "Payment using Card" button')
def step_impl(context):
    driver = get_driver_instance(context)
    payment = driver.find_element(AppiumBy.XPATH, '(//android.widget.LinearLayout[@resource-id="com.android.vending:id/0_resource_name_obfuscated"])[7]/android.widget.LinearLayout[2]')
    payment.is_displayed()
    payment.click()
    time.sleep(2)

@then('I should see "Add Credit Card or Debit Card" Option')
def step_impl(context):
    driver = get_driver_instance(context)
    payment = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Add credit or debit card"]')
    assert payment.is_displayed()
    assert payment.text == 'Add credit or debit card'
    payment.click()
    time.sleep(2)

@when('I should see "Card Number" Field')
def step_impl(context):
    driver = get_driver_instance(context)
    payment = driver.find_element(AppiumBy.XPATH, '//android.widget.AutoCompleteTextView[@text="Card number"]')
    assert payment.is_displayed()
    assert payment.text == 'Card number'
    time.sleep(2)

@then('I click on "Card Number" and Enter "{cardNumber}"')
def step_impl(context,cardNumber):
    driver = get_driver_instance(context)
    payment = driver.find_element(AppiumBy.XPATH, '//android.widget.AutoCompleteTextView[@text="Card number"]')
    assert payment.text == 'Card number'
    payment.send_keys(cardNumber)
    time.sleep(2)

@when('I should see "MM/YY" Field')
def step_impl(context):
    driver = get_driver_instance(context)
    payment = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Expiry date, 2-digit month, 2-digit year"]')
    assert payment.is_displayed()
    assert payment.text == 'Expiry date, 2-digit month, 2-digit year'
    time.sleep(2)

@then('I click on "MM/YY" and Enter "{month_year}"')
def step_impl(context,month_year):
    driver = get_driver_instance(context)
    payment = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@text="Expiry date, 2-digit month, 2-digit year"]')
    payment.send_keys(month_year)
    time.sleep(2)

@when('I should see "CVV" Field')
def step_impl(context):
    driver = get_driver_instance(context)
    payment = driver.find_element(AppiumBy.XPATH, '//android.widget.AutoCompleteTextView[@text="CVV"]')
    assert payment.is_displayed()
    time.sleep(2)

@then('I click "CVV" and Enter "{cvv}"')
def step_impl(context,cvv):
    driver = get_driver_instance(context)
    payment = driver.find_element(AppiumBy.XPATH, '//android.widget.AutoCompleteTextView[@text="CVV"]')
    payment.send_keys(cvv)
    time.sleep(2)


@when('I should see "Payment Amount"')
def step_impl(context):
    driver = get_driver_instance(context)
    payment_Amount = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="₹4,600.00/month"]')
    assert payment_Amount.is_displayed()
    time.sleep(2)

@then('I click on "Save Card" button')
def step_impl(context):
    driver = get_driver_instance(context)
    SaveCard = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@text="Save card"]')
    assert SaveCard.is_displayed()
    SaveCard.click()
    time.sleep(2)



# ------------- Scenario for Payment Process if needed then ... --------------

# Scenario: Payment Process 
#     Given I should see "Payment" Popup Modal
#     When I should see "Payment using Card" Option
#     Then I click on "Payment using Card" button
#     Then I should see "Add Credit Card or Debit Card" Option
#     When I should see "Card Number" Field
#     Then I click on "Card Number" and Enter "4242424242424242"
#     When I should see "MM/YY" Field
#     Then I click on "MM/YY" and Enter "10/25"
#     When I should see "CVV" Field
#     Then I click "CVV" and Enter "123"
#     When I should see "Payment Amount" 
#     Then I click on "Save Card" button

#  ------------------------

# @when('I see all available subscription plans listed below')
# def step_impl(context):
#     driver = get_driver_instance(context)

#     subscription_plan = {
#             'less than 25 head' : [
#                 'Monthly\n₹820.00\n1 Month Amnesty',
#                 'Annual\n₹3,350.00\n₹6,700.00\n3 Month Amnesty'
#             ],
#             'Between 26 and 50 head' : [
#                 'Monthly\n₹1,400.00\n1 Month Amnesty',
#                 'Annual\n₹5,600.00\n₹11,200.00\n3 Month Amnesty'
#             ],
#             'Between 51 and 100 head' : [
#                 'Monthly\n₹2,100.00\n1 Month Amnesty',
#                 'Annual\n₹9,200.00\n₹18,400.00\n3 Month Amnesty'
#             ],
#             'Between 101 and 300 head' : [
#                 'Monthly\n₹4,600.00\n1 Month Amnesty',
#                 'Annual\n₹22,350.00\n₹44,700.00\n3 Month Amnesty'
#             ],
#             'Between 301 and 1000 head': [
#                 'Monthly\n₹10,300.00\n1 Month Amnesty',
#                 'Annual\n₹42,000.00\n₹84,000.00\n3 Month Amnesty'
#             ]
#         }
#     for i in subscription_plan:
#         assert driver.find_element(AppiumBy.ACCESSIBILITY_ID, i).is_displayed()

#         if(i == 'Monthly\n₹820.00\n1 Month Amnesty'):
#             checkBox = driver.find_element(AppiumBy.XPATH,'//android.view.View[@content-desc="Monthly ₹820.00 1 Month Amnesty"]/android.widget.CheckBox')
#             checkBox.click()
#             time.sleep(3)

#         time.sleep(1)
#     def scroll_down():
#         driver.execute_script("mobile: scrollGesture", {
#             "left": 100, "top": 100, "width": 200, "height": 1200,
#             "direction": "down",
#             "percent": 1.0
#         })

#     scroll_down()
#     time.sleep(2)






# Scenario: Verify Manage Subscription Page Features
#     Given I am on the Manage Subscription Page
#     When I see the "Features Description" at the top of the screen
#     Then I verify that "Limited Offer" is displayed
#     When I see all available subscription plans listed below
#     When I verify that the "Select Plan and Subscribe" button is visible
#     Then I click on "Pay ₹4,600.00" button
#     Then I should see PopUp Box





