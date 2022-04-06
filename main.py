#from register import *
from flask import Flask, jsonify
from flask_restful import Resource, Api


load_dotenv()



#inputs || time in text format. may need to change later. 
registration_time = '03:00 PM'
event = 'WEC'

class status(Resource):    
     def get(self):
         try:
            return {'data': 'Api running'}
         except(error): 
            return {'data': error}


#adds ublock for ad blocking
op = Options()
op.add_extension(r'C:\CSProjects\gym-registration\ublock.crx')


<<<<<<< HEAD
#sets up chrome browser
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=op)

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

#find_event will fail if next_day is used since XPATH is different for the next day's page --> work on making find_event reactive?
def next_day():
    try:
        next = driver.find_element(by=By.XPATH, value='//*[@id="imlBodyMain"]/div/div[1]/div[2]/div[1]/div/div[5]/week-calendar/div[1]/div[1]/table/tbody/tr/td[1]/table/tbody/tr/td[1]/div/button[2]')
        next.click()
    except:
        print("next_day failed")

def find_event(registration_time, event_name):
    try:
        event_names = driver.find_elements(by=By.XPATH, value='//*[@id="imlBodyMain"]/div/div[1]/div[2]/div[1]/div/div[5]/week-calendar/div[2]/div[2]/div/div')
        index = 0
        for x in range(len(event_names)):
            text = event_names[x].text
            if (event_name in text and registration_time in text):
                index = x
    except:
        print("event_names could not generate")
        driver.quit()
        exit()
    try: 
        targeted_button = driver.find_element(by=By.XPATH, value = '//*[@id="imlBodyMain"]/div/div[1]/div[2]/div[1]/div/div[5]/week-calendar/div[2]/div[2]/div/div[' + str(index+1) +']/a/div/div[2]/div[1]/button' )
        targeted_button.click()
    except:
        print("find_event failed")
        driver.quit()
        exit()

def login():    
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@title="Select School/Organization"]')))
        dropdown = driver.find_element(by=By.XPATH, value = '//*[@title="Select School/Organization"]')
        dropdown.click()
    except:
        print('school dropdown not being found')
        driver.quit()
        exit()

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@title="search box"]')))
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

def sign_up():
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[3]/div[1]/div[11]/div/div[2]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/div/div/button')))
        sign_up_button2 = driver.find_element(by=By.XPATH, value = '/html/body/div[3]/div[1]/div[11]/div/div[2]/div/div[1]/div[2]/div[1]/div/div/div[2]/div[3]/div/div/button')
        sign_up_button2.click()
    except:
        print('sign up button not found or working')
        driver.quit()
        exit()

def registerForEvent(registrationTime, eventToRegister):
    registration_time = registrationTime 
    event_name = events[eventToRegister] 
    open_webpage()
    find_event(registration_time, event_name)
    login()
    sign_up()

=======
>>>>>>> origin/master
