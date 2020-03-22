# MyObservatoryTest
A sample UI automation test script demo for MyObservatory App

Setup guide
1.First of all,you are required to download and install Appium Server, and then start the server. For more information: http://appium.io/
2.use python 3.x,then install appium-client package
3.run test/test_9day.py 

Description:
This is a Ui automation test script sample for MyObservatory App using python,it's shown how 9-Day Forecast menu be clicked and assert the content inside.
It's divided into 3 page Nightdayforcastpage , MainPage and BasePage.
Nightdayforcastpage extends Base Page，which contain specific 9 day forcecast detail element and operation in it.
MainPage extends Base Page,which contains the menu .
BasePage contains some basic operation.
NightDayTest is the testcase to test Nightdayforcastpage.