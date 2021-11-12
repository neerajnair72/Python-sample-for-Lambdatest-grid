import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context

from threading import Thread
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.mobileby import MobileBy
from appium import webdriver


# This array 'caps' defines the capabilities browser, device and OS combinations where the test will run
caps = [

    {
        "deviceName": "Galaxy Tab S4",
        # "appPackage": "org.wikipedia",
        # "appActivity": ".main.MainActivity",
        "platformName": "android",
        "platformVersion": "10",
        "app": "lt://APP10020211636713412746351",
        # "infraTimeout": 100,
        "isRealMobile": True,
        # "tunnel": True,
        "deviceOrientation": "PORTRAIT",
        "visual": True,
        "console": True,
        "build": "Demo",
        # "devicelog": True,
        # "tunnel": True,
        #  "geoLocation": "BR",
    },
]
# run_session function searches for 'lambtest' on google.com


def run_session(desired_cap):
    driver = webdriver.Remote(
        # hub.mobile-dev-1.dev.lambdatest.io/wd/hub",
        command_executor="https://shubhamr:bKCQ8wHNM5QHi8m3c9vc9JecZjXeWN34SfNIEBYZywYAPoC87Z@beta-hub.lambdatest.com/wd/hub",
        desired_capabilities=desired_cap)

    # driver.get("https://www.ifconfig.me")
    # time.sleep(10)
    # Test case for the lambdatest sample Android app.
# If you have uploaded your app, update the test case here.
    search_element = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (MobileBy.ACCESSIBILITY_ID, "Search Wikipedia"))
    )
    search_element.click()
    search_input = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable(
            (MobileBy.ID, "org.wikipedia.alpha:id/search_src_text"))
    )
    search_input.send_keys("lambdatest")
    time.sleep(5)
    search_results = driver.find_elements_by_class_name(
        "android.widget.TextView")
    assert(len(search_results) > 0)

# Invoke driver.quit() after the test is done to indicate that the test is completed.
    driver.quit()


# The Thread function takes run_session function and each set of capability from the caps array as an argument to run each session in parallel
for cap in caps:
    Thread(target=run_session, args=(cap,)).start()