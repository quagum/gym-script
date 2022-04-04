from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time
from dotenv import load_dotenv
import os

load_dotenv()

#inputs
#time in text format. may need to change later. 
registration_time = '05:00 PM'
event = 'WEC'

email = os.getenv("email")
print(email)

#validate time input, exits if incorrect (could use a bit more fixing like checking if hour is valid)
try:
    assert len(registration_time) == 8 and ('PM' in registration_time or 'AM' in registration_time) and registration_time[2] == ':' 
    print('time format check passed')
except:
    print('time format is wrong')
    exit()

#add ublock for ad blocking
op = Options()
op.add_extension('./ublock.crx')
#remove notifcations popup
prefs = {"profile.default_content_setting_values.notifications" : 2}
op.add_experimental_option("prefs",prefs)

#set up chrome browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=op)

#open up webpage
driver.get("http://imleagues.com/spa/fitness/cbf1b9ddc23e46a78270684b9ce053da/home")

#wait until page is loaded to run, quit after 10 seconds if events aren't showing up
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "event-title")))
except:
    print('Page load error')
    driver.quit()
    exit()

#Full event names from shorthand
events = {'WEC': 'WEC Fitness Center Registration', 
          'Swim':'Open Swim', 
          'Honors':'Warren St. Fitness Center Registration', 
          'Tennis': 'Open Tennis Hours'}

event_name = events[event]

event_names = driver.find_elements(by=By.XPATH, value='//*[@id="imlBodyMain"]/div/div[1]/div[2]/div[1]/div/div[5]/week-calendar/div[2]/div[2]/div/div')
index = 0
for x in range(len(event_names)):
    text = event_names[x].text
    if (event_name in text and registration_time in text):
        index = x

print(index+1)

targeted_button = driver.find_element(by=By.XPATH, value = '//*[@id="imlBodyMain"]/div/div[1]/div[2]/div[1]/div/div[5]/week-calendar/div[2]/div[2]/div/div[' + str(index+1) +']/a/div/div[2]/div[1]/button' )
targeted_button.click()

#/html/body/div[3]/div[1]/div[11]/div/div[2]/div/div[1]/div[2]/div[1]/div/div[5]/week-calendar/div[2]/div[2]/div/div[30]/a/div/div[2]/div[1]/button


""" #main code
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
    
    #find a way to obtain event again by index. 
    #print(driver.find_element(By.xpath("//input[@class = 'event-text'][position()=8]")).text)
    
    #use "following" command to locate sign up button following appropriate event


    #current status: clicking 1st sign up button
    #click sign up button
    sign_up_button = driver.find_element(by=By.XPATH, value = '//*[@class="btn btn-success"]')
    print(sign_up_button.text)
    sign_up_button.click()

    input('press enter to continue')

except:
    print('could not find session to sign up for') """

try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@title="search box"]')))
except:
    print('Page load error')
    driver.quit()
    exit()

#sign in
try:
    dropdown = driver.find_element(by=By.XPATH, value = '//*[@title="Select School/Organization"]')
    dropdown.click()
except:
    print('school dropdown not being found')
    driver.quit()
    exit()


try:
    search_box = driver.find_element(by=By.XPATH, value = '//*[@title="search box"]')
    search_box.send_keys('NJIT')
    search_box.send_keys(Keys.RETURN)
except:
    print('school search not working')
    driver.quit()
    exit()



try:
    email_box = driver.find_element(by=By.XPATH, value = '//*[@name="email"]')
    email = os.getenv("email")
    email_box.send_keys(email)
    email_box.send_keys(Keys.RETURN)
except:
    print('email input not working')
    driver.quit()
    exit()


try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
except:
    print('password load error')
    
    driver.quit()
    exit()

try:
    password = os.getenv("password")
    password_box = driver.find_element(by=By.XPATH, value = '//*[@name="password"]')
    password_box.send_keys(password)
    password_box.send_keys(Keys.RETURN)
except:
    print('password not working')
    driver.quit()
    exit()

#Actually click sign up after login
#currently not working? 
#explicit wait may need editing
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div[1]/div[11]/div/div[2]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/div/div/button')))
except:
    driver.quit()
    exit()

sign_up_button2 = driver.find_element(by=By.XPATH, value = '/html/body/div[3]/div[1]/div[11]/div/div[2]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/div/div/button')
sign_up_button2.click()

try: 
    sign_up_button2 = driver.find_element(by=By.XPATH, value = '/html/body/div[3]/div[1]/div[11]/div/div[2]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/div/div/button')
    sign_up_button2.click()
except:
    print('sign up button not found or working')
    input('press enter to close browser')
    driver.quit()
    exit()

#keep browser open until button press (for testing only)
input('press enter to close browser')

#troll comment
#troll comment 2
