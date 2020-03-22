from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By

from page.BasePage import BasePage


class NightDayPage(BasePage):
    #定位器
    def __init__(self,driver):
        super().__init__(driver)
        self.local_fors_content = (By.ID,'hko.MyObservatory_v1_0:id/local_forecast_details')
        self.local_fors_icon = (By.ID,'hko.MyObservatory_v1_0:id/local_forecast_Icon')
        self.tab_local = (MobileBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Local Forecast")')
        self.SevenDayGenSit = (By.ID,'hko.MyObservatory_v1_0:id/mainAppSevenDayGenSit')
        self.SevenDayGenview = (By.ID,'hko.MyObservatory_v1_0:id/mainAppSevenDayView')
        self.max_temp_layout = (By.ID,'hko.MyObservatory_v1_0:id/extended_outlook_max_temp_layout')
        self.min_temp_layout = (By.ID,'hko.MyObservatory_v1_0:id/extended_outlook_min_temp_layout')
        self.mslp_layout = (By.ID,'hko.MyObservatory_v1_0:id/extended_outalook_mslp_layout')


    def switchto_local_forecast(self):
        #滑动到该tab，判断是否有元素
        #switch
        self.find_element_by_text('Local Forecast').click()
        detail_content = self.find_element(self.local_fors_content)
        detail_icon = self.find_element(self.local_fors_icon)

        return (detail_content,detail_icon)

    def switchto_night_day_forecast(self):
        self.find_element_by_text('9-Day Forecast').click()
        GenSit = self.find_element(self.SevenDayGenSit)
        GenSitView = self.find_element(self.SevenDayGenview)
        return (GenSit,GenSitView)

    def switchto_extended_outlook(self):
        self.find_element_by_text('Extended Outlook').click()
        max_temp = self.wait_element_display(self.max_temp_layout)
        min_temp = self.wait_element_display(self.min_temp_layout)
        mslp = self.wait_element_display(self.mslp_layout)
        return (max_temp,min_temp,mslp)

    def more_menu(self):
        pass