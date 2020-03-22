from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage(object):
    def __init__(self,driver:WebDriver):

        self.driver=driver


    def find_element(self, locator,parent=None):
        if parent:
            obj = parent.find_element(locator[0],locator[1])
        else:
            obj = self.driver.find_element(locator[0],locator[1])
        return obj

    def open_app(self):
        self.cap = {
            'platformName': 'Android',
            'appPackage': 'hko.MyObservatory_v1_0',
            'appActivity': 'hko.MyObservatory_v1_0.AgreementPage',
            'noReset': 'True'
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.cap)

    def find_by_scroll(self, item_name):
        item = self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().resourceId("hko.MyObservatory_v1_0:id/left_drawer").scrollable(true).instance(0)).getChildByText(new UiSelector().className("android.widget.TextView"), "'
            + item_name + '",true)')
        return item

    def find_element_by_text(self,txt):
        return self.driver.find_element_by_android_uiautomator('new UiSelector().text("'+txt+'")')

    def wait_element_display(self,location):
        try:
            WebDriverWait(timeout=30, driver=self.driver).until(
                EC.visibility_of_element_located(location))
            return True
        except TimeoutException:
            return False


