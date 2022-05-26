from atexit import register
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from dotenv import load_dotenv
import tkinter as tk
import os
import time

#--------------------------
#---=== DRIVER SETUP ===---
#--------------------------

#NEED TO HARDCODE EXTENSION PATH 
#adds ublock for ad blocking 
#necessary for low page load times
op = Options()
op.add_extension('ublock.crx')

#removes notifcations popup
prefs = {"profile.default_content_setting_values.notifications" : 2, 
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False}
op.add_experimental_option("prefs",prefs)

#sets up chrome browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=op)

#---------------------
#---=== METHODS ===---
#---------------------
def time_formatter(input_time):
    #validate time input, exits if incorrect
    #could use a bit more fixing like checking if hour is valid
    try:
        assert len(input_time) == 8 and ('PM' in input_time or 'AM' in input_time) and input_time[2] == ':' 
        print('time format valid')
        register_time = input_time 
        return register_time
    except:
        print('time format invalid')
        exit()
def event_formatter(input_event):
    events = {'WEC': 'WEC Fitness Center Registration', 
        'Swim':'Open Swim', 
        'Honors':'Warren St. Fitness Center Registration', 
        'Tennis': 'Open Tennis Hours'}
    try:
        assert input_event in events
        #converts from shorthand to proper full event names used by imleagues
        register_event = events[input_event]
        print('event format is valid')
        return register_event
    except:
        print('event format invalid')
        exit()

def open_webpage():
    #open up webpage
    driver.get("http://imleagues.com/spa/fitness/cbf1b9ddc23e46a78270684b9ce053da/home")
    driver.maximize_window()
    #wait until page is loaded to run, quit after 10 seconds if events aren't showing up
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "event-title")))
    except:
        print('Page load error')
        driver.quit()
        exit()

def next_day():
    #CURRENTLY NOT IN USE
    #made to switch to a different day's page to scrape 
    #find_event will fail if next_day is used since XPATH is different for the next day's page 
    #work on making find_event reactive?

    try:
        next = driver.find_element(by=By.XPATH, value='//*[@id="imlBodyMain"]/div/div[1]/div[2]/div[1]/div/div[5]/week-calendar/div[1]/div[1]/table/tbody/tr/td[1]/table/tbody/tr/td[1]/div/button[2]')
        next.click()
    except:
        print("next_day failed")

def find_event(register_time, event_name):
    try:
        event_names = driver.find_elements(by=By.XPATH, value='//*[@id="imlBodyMain"]/div/div[1]/div[2]/div[1]/div/div[5]/week-calendar/div[2]/div[2]/div/div')
        index = 0
        for x in range(len(event_names)):
            text = event_names[x].text
            if (event_name in text and register_time in text):
                index = x
    except:
        print("event_names could not generate")
        driver.quit()

    try: 
        targeted_button = driver.find_element(by=By.XPATH, value = '//*[@id="imlBodyMain"]/div/div[1]/div[2]/div[1]/div/div[5]/week-calendar/div[2]/div[2]/div/div[' + str(index+1) +']/a/div/div[2]/div[1]/button' )
        targeted_button.click()
    except:
        print("event is not available")
        driver.quit()

def login():   
    load_dotenv() 
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@title="Select School/Organization"]')))
        dropdown = driver.find_element(by=By.XPATH, value = '//*[@title="Select School/Organization"]')
        dropdown.click()
    except:
        print('school dropdown not being found')
        driver.quit()

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@title="search box"]')))
        search_box = driver.find_element(by=By.XPATH, value = '//*[@title="search box"]')
        search_box.send_keys('NJIT')
        search_box.send_keys(Keys.RETURN)
    except:
        print('school search not working')
        driver.quit()

    try:
        email_box = driver.find_element(by=By.XPATH, value = '//*[@name="email"]')
        email = os.getenv("email")
        email_box.send_keys(email)
        email_box.send_keys(Keys.RETURN)
    except:
        print('email input not working')
        driver.quit()

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
    except:
        print('password inputbox load error')
        driver.quit()

    try:
        password = os.getenv("password")
        password_box = driver.find_element(by=By.XPATH, value = '//*[@name="password"]')
        password_box.send_keys(password)
        password_box.send_keys(Keys.RETURN)
    except:
        print('password input not working')
        driver.quit()

def sign_up():
    try:
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div[1]/div[11]/div/div[2]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/div/div/button')))
        sign_up_button2 = driver.find_element(by=By.XPATH, value = '/html/body/div[3]/div[1]/div[11]/div/div[2]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/div/div/button')
        sign_up_button2.click()
    except:
        print('sign up button not found or working')
        driver.quit()

def popup():
    window = tk.Tk() 
    window.title("Success!")
    label = tk.Label(window, text="Signed Up!")
    label.pack(side="top", fill="x", pady=10)
    exit = tk.Button(window, text="Close", command = window.destroy)
    exit.pack()
    window.mainloop()

def run(input_time, input_event):
    try: 
        register_time = time_formatter(input_time)
        register_event = event_formatter(input_event)
        open_webpage()
        find_event(register_time, register_event)
        login()
        sign_up()
        popup()
        driver.quit()
    except:
        exit

#------------------
#---=== MAIN ===---
#------------------
run("02:30 PM", "WEC")
