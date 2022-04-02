from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager



op = Options()
op.add_extension('./ublock.crx')

#currently for chrome v100
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=op)
#driver = webdriver.Chrome(r"./chromedriver", options=op)

driver.get("http://imleagues.com/spa/fitness/cbf1b9ddc23e46a78270684b9ce053da/home")

time.sleep(5)

#driver.maximize_window()
#time.sleep(10)

#time in text format. may need to change later. 
registration_time = '03:00 PM'
event = 'WEC'

try:
    assert len(registration_time) == 8 and ('PM' in registration_time or 'AM' in registration_time) and ':' in registration_time
    print('time format check passed')
except:
    print('time format is wrong')

events = {'WEC': 'WEC Fitness Center Registration', 
          'Swim':'Open Swim', 
          'Honors':'Warren St. Fitness Center Registration', 
          'Tennis': 'Open Tennis Hours'}

event_name = events[event]

try:
    event_names = driver.find_elements(by=By.CLASS_NAME, value="event-title")
    times = driver.find_elements(by=By.CLASS_NAME, value="event-text")
    print(len(event_names), len(times))
    event_list = []
    for i in range(len(event_names)):
        event_list.append([event_names[i].text,times[i*2+1].text])
    
    for item in event_list:
        print(item)

    #check if item exists, get index if possible. 
    event_number = None
    for i in range(len(event_list)):
        if (event_list[i][0]==event_name and event_list[i][1]==registration_time):
            event_number = i+1
            break
    print('requested event:', event_name, registration_time)
    print('found event:', event_number, event_list[event_number-1])
    
    #print(event_number, event_list[event_number-1])
    #print(driver.find_element(By.xpath("//input[@class = 'event-text'][position()=8]")).text)
    

    

except:
    print('could not find element')

#keep browser open until button press
input('press enter to close browser')


