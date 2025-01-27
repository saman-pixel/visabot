from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

    # Path to your ChromeDriver
chrome_driver_path = r'C:\Users\DELL\Downloads\chromedriver-win64\chromedriver.exe'

    # Replace these credentials with your own
email = "bhattaraianil507"
domain ="gmail.com"
password = "Anil@1234567"
name = "bhattaraianil507@gmail.com"
phone = "9806247188"

    # Initialize ChromeOptions
options = webdriver.ChromeOptions()

    # Initialize WebDriver with Service object
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=options)

try:
        #open the page
        driver.get("https://www.g4k.go.kr/en/main.do")
        print("Website loaded successfully!")
        driver.maximize_window()
        language_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "btnLang"))
        )
        
        # Modify the text
        driver.execute_script("arguments[0].innerText = '언어 선택';", language_button)
        
        # Optional: Click the button if it triggers a language change
        language_button.click()
        # korean_button.click()
        time.sleep(2)

        # Step 3: Click on "로그인"
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "로그인"))  # Korean text for login
        )
        login_button.click()
        time.sleep(5)
        print("언어가 한국어로 변경되었습니다!")
        member_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "memberLogin"))
        )
        member_button.click()
       # Step 3: Enter login credentials
        # Locate the username and password fields
        # captcha =input("Enter captcha:")
        # print("sleeping")
        # time.sleep(5)
        #name_field = WebDriverWait(driver, 10).until(
        #    EC.presence_of_element_located((By.ID, "mberNm"))  # Replace with actual field ID
        #)
        # password_field = driver.find_element(By.ID, "loginPwd")  # Replace with actual field ID
        # captcha_field =driver.find_element(By.ID,"captchaTxt")
        # email_field =driver.find_element(By.ID,"emailId")
        # domain_field =driver.find_element(By.ID,"emailDomn")
        # Input your credentials (replace 'your_username' and 'your_password')
        #username_field.send_keys(email)
        #password_field.send_keys(password)
        #captcha_field.send_keys(captcha)
        #domain_field.send_keys(domain)
        # name_field.send_keys(name)   
        #time.sleep(5)
        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "loginId"))  # Replace if necessary
        )
        name_input.send_keys(name)
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "loginPwd"))  # Replace if necessary
        )
        password_input.send_keys(password)


        # email_input = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.ID, "emailId"))  # Replace if necessary
        # ) 
        # email_input.send_keys(email)
        # email_domain_input = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.ID, "emailDomn"))  # Replace if necessary
        # )
        # email_domain_input.send_keys(domain)
        # phone_input = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.ID, "smsNo"))  # Replace if necessary
        # )
        # phone_input.send_keys(phone)
        time.sleep(5)
        # submit_button = WebDriverWait(driver, 10).until(
        #    EC.element_to_be_clickable((By.ID,"btn_login"))
        # )

        # captcha =input("Enter captcha:")
        # print("sleeping")
        # captcha.send_keys(captcha)
        captcha_input = driver.find_element(By.ID, "captchaTxt")
        print("sleeping")
        captcha = input("Enter the CAPTCHA value manually: ") 
        captcha_input.send_keys(captcha)
        time.sleep(5)
        submit_button = WebDriverWait(driver, 10).until(
           EC.element_to_be_clickable((By.ID,"btn_login"))
        )
        submit_button.click() 
        print("Login successful!")
        time.sleep(5)
         # Click the login button
        # country_dropdown = WebDriverWait(driver, 10).until(
        #     lambda driver: driver.find_element(By.ID, "mberTelFg"))  # Replace with actual dropdown ID    
        
        # # Create a Select object for interacting with the dropdown
        # select = Select(country_dropdown)
        
        # # Select a country by visible text
        # select.select_by_value("네팔")  # Replace with the desired country name
        # submit_button.click()

        # Step 8: Wait for redirection after login
        
        # print("Login successful!")
        # time.sleep(5)

        # eng_button = WebDriverWait(driver, 10).until(
        # EC.visibility_of_element_located((By.CLASS_NAME, "btnLang"))
        # )
        
        # # Modify the text
        # driver.execute_script("arguments[0].innerText = '언어 선택';", eng_button)
        
        # # Optional: Click the button if it triggers a language change
        # eng_button.click()
        # # korean_button.click()
        # time.sleep(2)
        # english_button = WebDriverWait(driver, 10).until(
        #     EC.element_to_be_clickable((By.LINK_TEXT, "ENG"))
        # )
        # english_button.click()
        # time.sleep(5)
        
        driver.get("https://www.g4k.go.kr/ciph/0800/selectCIPH0801Deng.do")
        print("Reservation loaded successfully!")

    # Click the link
        # Reserv_link.click()
        # print(driver.page_source)

 # Click the link
        button = driver.find_element(By.XPATH, "//button[contains(text(), 'Make a Reservation')]")
        button.click()
        time.sleep(10)

        region_dropdown = Select(driver.find_element(By.ID, "visitRegnCd"))  # Replace with actual ID or locator
        region_dropdown.select_by_value('EE')   # Select by value
        time.sleep(5)
           
        # region_dropdown = driver.find_element(By.ID, "visitRegnCd")
        # driver.execute_script("arguments[0].value = 'BB';", region_dropdown)
        # driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", region_dropdown)

# Wait for the nation dropdown to be clickable and select a nation
        driver.execute_script("arguments[0].style.display = 'block'; arguments[0].disabled = false;", driver.find_element(By.ID, "visitNatnCd"))
        WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "visitNatnCd"))  # Replace with the actual ID
    )

    # Step 3: Select a Country from the Updated Dropdown
        
        country_dropdown = Select(driver.find_element(By.ID, "visitNatnCd"))
        country_dropdown.select_by_value("321")  # Example: Selecting 'INDIA'
        time.sleep(5)
#         nation_dropdown = driver.find_element(By.ID, "visitNatnCd")

# # Set the value to "124" (INDIA)
#         driver.execute_script("arguments[0].value = '124';", nation_dropdown)
#         driver.execute_script("arguments[0].dispatchEvent(new Event('change'));", nation_dropdown)

# Wait for the consulate/embassy dropdown to be clickable and select a consulate/embassy
        driver.execute_script("arguments[0].style.display = 'block'; arguments[0].disabled = false;", driver.find_element(By.ID, "visitEmblCd"))
        consulate_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "visitEmblCd"))
        
)       
        consulate_dropdown = Select(driver.find_element(By.ID, "visitEmblCd"))
        consulate_dropdown.select_by_visible_text(
        "[FRANCE] Embassy of the Republic of Korea to the French Republic"
 )  # Example: Selecting 'INDIA'
        time.sleep(10)
#         Select(consulate_dropdown).select_by_visible_text(
#         "[INDIA] Embassy of the Republic of Korea to the Republic of India"
# )

# # Submit the form
#         form = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "emblForm"))
# )
#         form.submit()
#         print("Form submitted successfully!")

# Wait for the next button to be clickable and click it
        next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "aftBtn"))
)
        next_button.click()
        print("Successful!")
# # Use execute_script to simulate a click
#         driver.execute_script("arguments[0].click();", link_element)

# Click the anchor tag (<a>) to navigate
        

# Wait for 2 seconds (you can adjust or replace this with WebDriverWait for better reliability)
        # time.sleep(2)
    #     reservation_button = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.CLASS_NAME, "btn.dBlue"))
    # )

    # Click the button
        # reservation_button.click()

        # print("Button clicked successfully!")
        # time.sleep(5)

        # Locate the dropdown element by its ID (or other locator)
        # dropdown = Select(driver.find_element(By.ID, "dropdown_id"))  # Replace "dropdown_id" with the actual ID of the dropdown

        # Select an option by its visible text (name)
        # dropdown.select_by_visible_text("Nepal")  # Replace "Option Name" with the actual text of the option you want to select
        

except Exception as e:
        print(f"An error occurred: {e}")

finally:
        # Close the browser
        driver.quit()