# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 20:01:37 2025

@author: Lenovo
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# from seleniumbase import SB
email= "iamsama17@gmail.com"
password = "saman213u85"
# Path to your ChromeDriver
chrome_driver_path = r'C:\Users\Lenovo\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'

# Initialize ChromeOptions
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Open browser in maximized mode
options.add_argument("--disable-blink-features=AutomationControlled")  # Bypass detection

# Initialize WebDriver with Service object
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

try:
    # Open the main page
    driver.get("https://visa.vfsglobal.com/npl/en/hrv/login")
    print("Website loaded successfully!")

    name_input = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.ID, "email"))  # Replace if necessary
     )
    name_input.send_keys(email)
    name_input = WebDriverWait(driver, 10).until(
         EC.presence_of_element_located((By.ID, "password"))  # Replace if necessary
     )
    name_input.send_keys(password)
    time.sleep(5)
    # with SB(uc=True, test=True) as sb:
    #     url = "https://seleniumbase.io/apps/turnstile"
    #     sb.uc_open_with_reconnect(url, reconnect_time=2)
    #     sb.uc_gui_handle_captcha()
    #     sb.assert_element("img#captcha-success", timeout=3)
    #     sb.set_messenger_theme(location="top_left")
    #     sb.post_message("SeleniumBase wasn't detected", duration=3)
       # with SB(uc=True, test=True, ad_block=True) as sb:
       #     url = "https://www.thaiticketmajor.com/concert/"
       #     sb.uc_open_with_reconnect(url, 6.111)
       #     sb.uc_click("button.btn-signin", 4.1)
       #     sb.uc_gui_click_captcha()

except Exception as e:
    print("An error occurred:", e)

finally:
    # Keep browser open for debugging (Press Enter to close)
    input("Press Enter to close the browser...")
    driver.quit()
