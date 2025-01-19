    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import Select
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import time

    # Path to your ChromeDriver
    chrome_driver_path = r'C:\Users\MSI\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'

    # Replace these credentials with your own
    email = "bhattaraianil507"
    domain ="gmail.com"
    password = "Anil@123456"
    name = "Anil Bhattarai"
    phone = "976588243"

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
        non_member_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "nonmemberLogin"))
        )
        non_member_button.click()
       # Step 3: Enter login credentials
        # Locate the username and password fields
        captcha =input("Enter captcha:")
        print("sleeping")
        time.sleep(5)
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
            EC.presence_of_element_located((By.ID, "mberNm"))  # Replace if necessary
        )
        name_input.send_keys(name)

        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "emailId"))  # Replace if necessary
        ) 
        email_input.send_keys(email)
        email_domain_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "emailDomn"))  # Replace if necessary
        )
        email_domain_input.send_keys(domain)
        phone_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "smsNo"))  # Replace if necessary
        )
        phone_input.send_keys(phone)
        time.sleep(5)
        submit_button = WebDriverWait(driver, 10).until(
           EC.element_to_be_clickable((By.ID,"crtfKeyNoBtn"))
        )
        country_dropdown = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element(By.ID, "mberTelFg"))  # Replace with actual dropdown ID    
        
        # Create a Select object for interacting with the dropdown
        select = Select(country_dropdown)
        
        # Select a country by visible text
        select.select_by_value("NP")  # Replace with the desired country name
        submit_button.click()

        # Step 8: Wait for redirection after login
        time.sleep(5)
        print("Login successful!")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser
        driver.quit()
