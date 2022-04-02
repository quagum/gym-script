from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager



op = Options()
op.add_extension('./ublock.crx')

#currently for chrome v100
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=op)
#driver = webdriver.Chrome(r"./chromedriver", options=op)

#need to fix? 
#selenium.common.exceptions.WebDriverException: Message: tab crashed
driver.get("http://imleagues.com/spa/fitness/cbf1b9ddc23e46a78270684b9ce053da/home")

time.sleep(10)

#driver.maximize_window()
#time.sleep(10)

registration_time = 16
event = 'WEC'

events = {'WEC': 'WEC Fitness Center Registration', 
          'Swim':'Open Swim', 
          'Honors':'Warren St. Fitness Center Registration', 
          'Tennis': 'Open Tennis Hours'}

event_name = events[event]

try:
    event_row = driver.find_element_by_class_name('event-item bottom-line')
    #event_row = driver.find_element(by=By.CLASS_NAME, value = "event-item bottom-line")
    event_row = driver.find_element(by=By.CLASS_NAME, value=name)

    text = event_row.text

    print(text)
except:
    print('could not find element')

#class="event-item bottom-line" <- class name of div for each sign up row

