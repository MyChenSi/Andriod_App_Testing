from appium import webdriver
 
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
el2 = driver.find_element_by_id("0b9c3d34-e4fc-4205-b8af-c2b788e197db")
el2.click()

 
driver.quit()