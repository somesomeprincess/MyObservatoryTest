from selenium.webdriver.common.by import By

from page.BasePage import BasePage


class MainPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)
        self.actionbar = (By.ID,'hko.MyObservatory_v1_0:id/action_bar')
        self.menu = (By.CLASS_NAME,'android.widget.ImageButton')


    def click_menu(self):
        obj_action_bar = self.find_element(self.actionbar)
        obj_menu = self.find_element(self.menu,parent = obj_action_bar)
        obj_menu.click()
        # actionbar = self.driver.find_element(By.ID, 'hko.MyObservatory_v1_0:id/action_bar')
        # menu = actionbar.find_element_by_class_name('android.widget.ImageButton')
        # menu.click()

    def click_9day_forcase_menu(self):
        night_day = self.find_by_scroll('9-Day Forecast')
        if night_day:
            night_day.click()
