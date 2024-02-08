import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

# Set desired capabilities for the Appium session
capabilities = {
    'platformName': 'Android',
    'deviceName': 'V2312',  # Replace 'Your_Device_Name' with the name of your real device
    'appPackage': 'io.appium.android.apis',    # Replace 'com.example.app' with the package name of your app
    'appActivity': 'io.appium.android.apis.ApiDemos',  # Replace 'com.example.app.MainActivity' with the main activity of your app
    'automationName': 'UiAutomator2',   # Use UiAutomator2 for Android automation,
    'language':'en',
    'locale':'US',
}

appium_server_url = 'http://localhost:4723'
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(command_executor=appium_server_url,options=capabilities_options)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_find_battery(self) -> None:
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//*[@text="App"]')
        el.click()

if __name__ == '__main__':
    unittest.main()