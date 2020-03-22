import unittest
from appium import webdriver

from page.MainPage import MainPage
from page.Nightdayforcastpage import NightDayPage


class NightDayTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cap = {
            'platformName': 'Android',
            'appPackage': 'hko.MyObservatory_v1_0',
            'appActivity': 'hko.MyObservatory_v1_0.AgreementPage',
            'noReset': 'True'
        }
        cls.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=cap)
        cls.driver.implicitly_wait(30)
        cls.mainpage = MainPage(cls.driver)

    def setUp(self) -> None:
        self.mainpage.click_menu()
        self.mainpage.click_9day_forcase_menu()
        self.nightpage = NightDayPage(self.driver)

    def tearDown(self) -> None:
        pass

    def test_switchto_local_forecast(self):
        content,icon = self.nightpage.switchto_local_forecast()
        self.assertIsNotNone(content.text,"local_forecast is none!")
        self.assertIsNotNone(icon,"local_forecast icon is none!")

    # def test_click_into_9day(self):
    #     pass

    def test_switchto_night_day_forecast(self):
        gensit,gensitview = self.nightpage.switchto_night_day_forecast()
        self.assertIsNotNone(gensit.text,'gensit is none!')
        self.assertIsNotNone(gensitview,'gensitview is none!')

    def test_switchto_extended_outlook(self):
        max_temp,min_temp,mslp=self.nightpage.switchto_extended_outlook()
        self.assertTrue(max_temp,"max_temp is false")
        self.assertTrue(min_temp,"min_temp is false")
        self.assertTrue(mslp,"mslp is false")


if __name__ == '__main__':
    unittest.main()
