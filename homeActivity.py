import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy  # Import AppiumBy
import time
from appium.webdriver.common.touch_action import TouchAction

# Set desired capabilities for the Appium session
capabilities = {
    'platformName': 'Android',
    'deviceName': 'V2312',  # Replace 'Your_Device_Name' with the name of your real device
    'appPackage': 'com.app.smytten.debug',    # Replace 'com.example.app' with the package name of your app
    'appActivity': 'com.app.smytten.ui.home.mvvm.root.view.HomeActivity',  # Replace 'com.example.app.MainActivity' with the main activity of your app
    'automationName': 'UiAutomator2',   # Use UiAutomator2 for Android automation,
    'language':'en',
    'locale':'US',
}

appium_server_url = 'http://localhost:4723'
capabilities_options = UiAutomator2Options().load_capabilities(capabilities)

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(command_executor=appium_server_url, options=capabilities_options)

    def tearDown(self) -> None:
        if self.driver:
            time.sleep(10)
            self.driver.quit()

    def print_all_views(self) -> None:
        time.sleep(1)
        print()
        print("#################")
        print()
        textviews = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.TextView")

        # Print the text of each TextView element
        for textview in textviews:
            print("TextView Text:", textview.text)
        
        input_boxes = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")

        # Print the text of each input box
        for input_box in input_boxes:
            print("Input Box Text:", input_box.text)

        buttons = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.Button")
        # Print the text of each button
        for button in buttons:
            print("Button Text:", button.text)
        print()
        print("#################")
        print()
        time.sleep(1)
    
    def click_button_by_text(self, text: str)-> None:
        time.sleep(1)
        xpath = f'//*[@text="{text}"]'  # Dynamically construct XPath with the provided text
        el = self.driver.find_element(AppiumBy.XPATH, xpath)
        el.click()
        time.sleep(1)

    def use_input(self, text: str) -> None:
        time.sleep(1)

        # Find the EditText element
        edit_text = self.driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
        
        # Enter text into the EditText
        edit_text.send_keys(text)
        
        # Add a delay (optional)
        time.sleep(1)

    def scroll_by_amount(self, start_x, start_y, end_x, end_y):
        # Perform a swipe gesture to scroll by a certain amount
        time.sleep(1)
        self.driver.swipe(start_x, start_y, end_x, end_y)
        time.sleep(1)
    
    def dismiss_popup_by_tap(self, x, y):
        time.sleep(1)
        # Perform a tap gesture to dismiss the popup by touching outside of its area
        touch_action = TouchAction(self.driver)
        touch_action.tap(x=x, y=y).perform()
        time.sleep(1)


    def test_print_textviews_after_delay(self) -> None:
        print()
        self.print_all_views()


if __name__ == '__main__':
    unittest.main()