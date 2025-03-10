from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to your ChromeDriver
chrome_driver_path = r'C:\Users\DELL\Downloads\chromedriver-win64 (2)\chromedriver.exe'

# Initialize ChromeOptions
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Open browser in maximized mode
options.add_argument("--disable-blink-features=AutomationControlled")  # Bypass detection

# Initialize WebDriver with Service object
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

try:
    # Open the main page
    driver.get("https://visa.vfsglobal.com/npl/en/hrv")
    print("Website loaded successfully!")

    # Wait for page to fully load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    # Navigate to appointment booking page
    driver.get("https://visa.vfsglobal.com/npl/en/hrv/book-an-appointment")
    print("Booking registration page loaded successfully!")

    # Wait for appointment page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

except Exception as e:
    print("An error occurred:", e)

finally:
    # Keep browser open for debugging (Press Enter to close)
    input("Press Enter to close the browser...")
    driver.quit()
