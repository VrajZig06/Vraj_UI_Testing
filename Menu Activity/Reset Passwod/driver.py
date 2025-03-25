from appium import webdriver
from appium.options.common.base import AppiumOptions

def get_driver():
    options = AppiumOptions()
    
    options.load_capabilities({
        "appium:platformName": "Android",
        "platformVersion": "14.0",
        # "deviceName": "emulator-5554",
        "deviceName": "AQJBJZDYCASWVOC6",
        #"appPackage": "com.greenerherd.android",
        "appActivity": ".MainActivity",
        #"appWaitActivity": "com.greenerherd.greener_herd.*",  # Match any activity
        #"app": "/home/zt39/Desktop/ParthAutomation/GreenerHerd_app/apk/app-release.apk",
        "appium:automationName": "UiAutomator2",
        "appium:ignoreHiddenApiPolicyError": "true",
        "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": False,
        "uiautomator2ServerLaunchTimeout": 60000,  # Increase timeout to 60 seconds
        #"noReset": True,
        #"fullReset": False
    })

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    
    return driver


# from appium import webdriver
# from appium.options.common.base import AppiumOptions

# def get_driver():
#     # Set capabilities for Android/iOS devices and start Appium session
#     options = AppiumOptions()
    
#     options.load_capabilities({
#         "appium:platformName": "Android",
#         "platformVersion": "15.0",
#         "deviceName": "emulator-5554",
#         "appPackage": "com.greenerherd.android",
#         "appActivity": "com.greenerherd.greener_herd.MainActivity",
#         "appWaitActivity": "com.greenerherd.greener_herd.*",  # Add wildcard to match any activity
#         "app": "/home/zt39/Desktop/ParthAutomation/GreenerHerd_app/apk/app-release.apk",
#         "appium:automationName": "UiAutomator2",
#         "appium:ignoreHiddenApiPolicyError": "true",
#         "appium:newCommandTimeout": 30000,
#         "appium:connectHardwareKeyboard": True,
#         "noReset": True,
#         "fullReset": False
# })

#     driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    
#     return driver


# from appium import webdriver
# from appium.options.common.base import AppiumOptions

# def get_driver():
#     # Set capabilities for Android/iOS devices and start Appium session
#     options = AppiumOptions()
    
#     options.load_capabilities({
#         "appium:platformName": "Android",
#         "platformVersion": "9.0",
#         "deviceName": "BRB3Y18721024639",
#         #"appPackage": "com.greenerherd.android",
#         "appActivity": ".MainActivity",
#         #"app": "/home/zt39/Desktop/ParthAutomation/GreenerHerd_app/apk/GreenerHerd.apk",
#         "appium:automationName": "UiAutomator2",
#         "appium:ignoreHiddenApiPolicyError": "true",
#         "appium:newCommandTimeout": 3600,
#         "appium:connectHardwareKeyboard": True,
#         # "noReset": True,
#         # "fullReset": False
#     })

#     driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    
#     return driver
