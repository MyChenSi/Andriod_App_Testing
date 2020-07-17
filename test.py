from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
 
caps = {}
caps["platformName"] = "Android"
caps["platformVersion"] = "10"
caps["deviceName"] = "ALP_AL00"
caps["appPackage"] = "com.baidu.searchbox"
caps["appActivity"] = ".MainActivity"
caps["resetKeyboard"] = True
caps["unicodeKeyboard"] = True
 
driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)

el1 = driver.find_element_by_id("android:id/button1")
el1.click()
el2 = driver.find_element_by_id("com.baidu.searchbox:id/close_btn")
el2.click()
el5 = driver.find_element_by_id("com.baidu.searchbox:id/baidu_searchbox")
el5.click()
el8 = driver.find_element_by_id("com.baidu.searchbox:id/SearchTextInput")
el8.send_keys("test")
el9 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.TextView")
el9.click()
driver.quit()