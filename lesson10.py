from selenium import webdriver
import time 
import math

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    a = browser.find_element_by_id("num1").text
    b = browser.find_element_by_id("num2").text
    z = str(str(int(a)+int(b))

    


    browser.find_element_by_css_selector("[class='btn btn-default']").click()

finally:

    time.sleep(30)
   
    browser.quit()





