import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy  # Import AppiumBy
import time
from appium.webdriver.common.touch_action import TouchAction

def non_null_non_empty(someData) -> bool:
    if someData is None:
        return False
    
    elif isinstance(someData, list) and len(someData) > 0:
        return True
    
    elif isinstance(someData, str) and someData.strip() != "":
        return True
    
    return False
# Set desired capabilities for the Appium session
capabilities = {
    'platformName': 'Android',
    'deviceName': 'V2312',  # Replace 'Your_Device_Name' with the name of your real device
    'appPackage': 'com.app.smytten.debug',    # Replace 'com.example.app' with the package name of your app
    'appActivity': 'com.app.smytten.ui.auth.PreLoginActivity',  # Replace 'com.example.app.MainActivity' with the main activity of your app
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
        if non_null_non_empty(textviews):
            for textview in textviews:
                print("TextView Text:", textview.text)
            
        input_boxes = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")

        # Print the text of each input box
        if non_null_non_empty(input_boxes):
            for input_box in input_boxes:
                print("Input Box Text:", input_box.text)

        buttons = self.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.Button")
        # Print the text of each button
        if non_null_non_empty(buttons):
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
        if el is not None:
            el.click()
        time.sleep(1)
    
    def click_button_by_text_coordinates(self, text: str, area=(0.2, 0.2, 0.8, 0.8)):
        time.sleep(1)
         # Dynamically construct XPath with the provided text
        xpath = f'//*[@text="{text}"]'

        # Find elements within the specified area
        elements = self.driver.find_elements(AppiumBy.XPATH, xpath)
        for element in elements:
            rect = element.rect
            print(element.text)
            element_x = rect['x'] + rect['width'] / 2
            element_y = rect['y'] + rect['height'] / 2
            if area[0] <= element_x <= area[2] and area[1] <= element_y <= area[3]:
                element.click()
                return
        # If no matching element found in the specified area
        print(f"No element with text '{text}' found within the specified area.")
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


    def perform_login_activity(self) -> None:
        time.sleep(2)
        self.print_all_views()
        self.click_button_by_text("Get Started")

        self.print_all_views()
        self.use_input("9106608886")
        
        self.click_button_by_text("Send OTP")

        self.print_all_views()

        self.click_button_by_text("USE ANOTHER MOBILE NUMBER")
        self.print_all_views()
        self.click_button_by_text("NONE OF THE ABOVE")
        self.print_all_views()
        self.click_button_by_text("Send OTP")
        self.print_all_views()
        self.use_input("1")
        self.use_input("1")
        self.use_input("1")
        self.use_input("1")
        self.print_all_views()
        self.click_button_by_text("DON’T ALLOW")
        self.print_all_views()
        self.dismiss_popup_by_tap(500, 500)
        
        for i in range(5):
            self.scroll_by_amount(500,500, 100, 100)
        
        self.print_all_views()

    def perform_trial_front_activity(self) -> None:
        # self.click_button_by_text_coordinates("Trial", area=(0, 0.8, 1, 1))
        self.click_button_by_text("Trial")
        self.print_all_views()
        for i in range(20):
            self.scroll_by_amount(500,500, 100, 100)
        

    def test_activity(self) -> None:
        self.perform_login_activity()
        self.perform_trial_front_activity()




if __name__ == '__main__':
    unittest.main()