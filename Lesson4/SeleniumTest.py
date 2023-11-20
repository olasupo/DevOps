import time

from selenium.webdriver.common.by import By

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(60)

#driver.get("https://www.globaldevexperts.com/")
driver.get("https://translate.google.com/")
#print(driver.current_url) #to print the url of the opened page
#print(driver.title) #to print the title of the page
#print(driver.page_source) #to check for something missing in the html
#driver.close() #will close the active tab
#driver.quit() #closes all browsers and cleans up resources.
#driver.back() #navigate back
#driver.forward() #navigate forward
#driver.refresh() #refresh page



#cool = driver.find_element(By.ID, value='global-styles-inline-css') #ID, Name, Linktext, Partial LinkText, ClassName, Xpath
#expert = driver.find_element(By.CLASS_NAME, value='OPPzxe').send_keys("Test123")
#clicking = expert = driver.find_element(By.ID, value='some_values').click() #click and submit control
#submit = expert = driver.find_element(By.ID, value='some_values').submit() #only submit a form
#send_keys = expert = driver.find_element(By.ID, value='some_values').send_keys("Testing 123") #only submit a form

driver.find_element(By.CLASS_NAME,value="er8xn").send_keys("Hello")

#print(expert)
time.sleep(60) # Let the user actually see something!

#driver.quit()


