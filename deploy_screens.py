#!/usr/bin/python3.4
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

display_list = ['https://python.org', 'https://ditrapani.com.au', 'https://cloudflare.com']

def define_args():
    options = webdriver.ChromeOptions()
    chrome_arguments = ['--start-fullscreen','--ignore-certificate-errors']

    for argument in chrome_arguments:
        options.add_argument(argument)
    
    # Allows screens to stay open after the GET request has been completed
    options.add_experimental_option("detach", True) 
    return options

def deploy_screens(display_list, options):
    for index, website in enumerate(display_list):
        width, height = get_window_size(index)
        options.add_argument("--window-position=" +str(width) +  "," + str(height))

        driver = webdriver.Chrome(r'C:\chromedriver_win32\chromedriver.exe', chrome_options=options) 
        driver.get(website)
        try:
            username = driver.find_element_by_name("username")
            password = driver.find_element_by_name("password")
            username.send_keys('admin')
            password.send_keys('admin')
            password.send_keys(Keys.RETURN)
        except NoSuchElementException:
            pass 

def get_window_size(index):
    # Set to width resolution of the monitors
    default_width = 1920 
    # Will offset the spawn point of the browser
    width = 100 + (default_width * index) 
    # Set window height, only needed if not adding --start-fullscreen as an option
    height = 300
    return width, height 

options = define_args()
deploy_screens(display_list, options)
