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
registration_time = '09:00 PM'
event = 'WEC'

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

#remove notifications popup
prefs = {"profile.default_content_setting_values.notifications" : 2, 
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False}

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

#get correct event index
event_names = driver.find_elements(by=By.XPATH, value='//*[@id="imlBodyMain"]/div/div[1]/div[2]/div[1]/div/div[5]/week-calendar/div[2]/div[2]/div/div')
index = 0
for x in range(len(event_names)):
    text = event_names[x].text
    if (event_name in text and registration_time in text):
        index = x

print(index+1)

#click 1st sign up button with correct index
try:
    targeted_button = driver.find_element(by=By.XPATH, value = '//*[@id="imlBodyMain"]/div/div[1]/div[2]/div[1]/div/div[5]/week-calendar/div[2]/div[2]/div/div[' + str(index+1) +']/a/div/div[2]/div[1]/button' )
    targeted_button.click()
except:
    print('error clicking 1st sign up button')
    exit()

#wait for sign in page to load
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@title="search box"]')))
except:
    print('Page load error')
    driver.quit()
    exit()

#click school dropdown
try:
    dropdown = driver.find_element(by=By.XPATH, value = '//*[@title="Select School/Organization"]')
    dropdown.click()
except:
    print('school dropdown not being found')
    driver.quit()
    exit()

#enter school name
try:
    search_box = driver.find_element(by=By.XPATH, value = '//*[@title="search box"]')
    search_box.send_keys('NJIT')
    search_box.send_keys(Keys.RETURN)
except:
    print('school search not working')
    driver.quit()
    exit()

#enter email
try:
    email_box = driver.find_element(by=By.XPATH, value = '//*[@name="email"]')
    email = os.getenv("email")
    email_box.send_keys(email)
    email_box.send_keys(Keys.RETURN)
except:
    print('email input not working')
    driver.quit()
    exit()

#wait for password page to load
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
except:
    print('password load error')
    driver.quit()
    exit()

#enter password
try:
    password = os.getenv("password")
    password_box = driver.find_element(by=By.XPATH, value = '//*[@name="password"]')
    password_box.send_keys(password)
    password_box.send_keys(Keys.RETURN)
except:
    print('password not working')
    driver.quit()
    exit()

#wait for 2nd sign up page to load
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div[1]/div[11]/div/div[2]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/div/div/button')))
except:
    print('could not find element')
    driver.quit()
    exit()

#Actually click sign up after login
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
