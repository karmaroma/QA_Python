from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/math.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x_element = browser.find_element_by_id("input_value")
    x = x_element
    y = calc(x)

    input1 = browser.find_element_by_id("answer")
    input1.send_keys(y)
    option1 = browser.find_element_by_css_selector("[class='form-check-label']")
    option1.click()
    option2 = browser.find_element_by_css_selector("[for='robotsRule']")
    option2.click()


 	#input1 = browser.find_element_by_tag_name("first_name")
    #input1.send_keys("Ivan")
    #input2 = browser.find_element_by_name("last_name")
    #input2.send_keys("Petrov")
    #input3 = browser.find_element_by_class_name("firstname")
    #input3.send_keys("Smolensk")
    #input4 = browser.find_element_by_id("country")
    #input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("[class='btn btn-default']")
    button.click()

finally:

    time.sleep(30)
   
    browser.quit()



link = "http://suninjuly.github.io/find_link_text"

