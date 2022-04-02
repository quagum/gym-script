from selenium import webdriver
import time

#currently for chrome v100
driver = webdriver.Chrome(r"./chromedriver")

#need to fix? 
#selenium.common.exceptions.WebDriverException: Message: tab crashed
driver.get("http://imleagues.com/spa/fitness/cbf1b9ddc23e46a78270684b9ce053da/home")

time.sleep(5)

#driver.maximize_window()
#time.sleep(10)

registration_time = 16
event = 'WEC'

events = {'WEC': 'WEC Fitness Center Registration', 
          'Swim':'Open Swim', 
          'Honors':'Warren St. Fitness Center Registration', 
          'Tennis': 'Open Tennis Hours'}

event_name = events[event]

event_row = driver.find_element_by_class_name("event-item bottom-line")

text = event_row.text

print(text)

#class="event-item bottom-line" <- class name of div for each sign up row

