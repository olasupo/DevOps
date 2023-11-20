from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

driver = webdriver.Chrome(service=Service("/usr/local/bin/chromedriver"))

time.sleep(5) # Let the user actually see something!

print("This is Beautiful")