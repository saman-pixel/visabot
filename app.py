from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Path to your ChromeDriver
chrome_driver_path = r'C:\Users\DELL\Downloads\chromedriver-win64\chromedriver.exe'

# Replace these credentials with your own
email = "your_email@example.com"
password = "your_password"

# Initialize ChromeOptions
options = webdriver.ChromeOptions()

# Initialize WebDriver with Service object
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

try:
    #open the page
    driver.get("https://www.g4k.go.kr/en/main.do")
    print("Website loaded successfully!")

    # Step 2: Click on the Korean language button
    korean_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'KOR')]"))  # Update to match the Korean language button text
    )
    korean_button.click()
    time.sleep(2)

    # Step 3: Click on "로그인"
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.LINK_TEXT, "로그인"))  # Korean text for login
    )
    login_button.click()
    time.sleep(2)

    # Step 4: Agree to terms (if applicable)
    try:
        agree_all_checkbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='agree_all']"))
        )
        agree_all_checkbox.click()
    except Exception as e:
        print(f"Agree checkbox not found: {e}")

    # Step 5: Fill in the login form
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))  # Replace if necessary
    )
    email_input.send_keys(email)

    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password"))  # Replace if necessary
    )
    password_input.send_keys(password)

    # Step 6: Handle CAPTCHA manually
    print("Please solve the CAPTCHA manually in the browser...")
    time.sleep(15)

    # Step 7: Submit the form
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )
    submit_button.click()

    # Step 8: Wait for redirection after login
    time.sleep(5)
    print("Login successful!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
