from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import capsolver

# Initialize capsolver with your API key
capsolver.api_key = "CAP-17351F4BF89C9E67B0B039CA92B05143C4175506097F47FB2D0EB40252A9C16F"

# Load the inject.js file content
with open("inject.js", "r", encoding="utf-8") as f:
    inject_js_content = f.read()

    try:
        # Solve the Turnstile CAPTCHA
        solution = capsolver.solve({
            "type": "AntiTurnstileTaskProxyLess",  # Required. Use 'AntiTurnstileTask' if using proxies or 'AntiTurnstileTaskProxyLess' if not.
            "websiteKey": "0x4AAAAAAACYaM3U_Dz-4DN1",  # Required. The public key of the domain, often called the 'site key.'
            "websiteURL": "https://visa.vfsglobal.com/npl/en/hrv/login",  # Required. The URL where the CAPTCHA is located.
        })

        token = solution.get('token')
        print("CAPTCHA Solved Token:", token)

        # Start Selenium WebDriver
        chrome_driver_path = r'C:\Users\Lenovo\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'

        # Initialize ChromeOptions
        options = webdriver.ChromeOptions()
        service = Service(chrome_driver_path)
        driver = webdriver.Chrome(service=service, options=options)

        print(inject_js_content)

        # Inject JavaScript from local file
        driver.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument",
            {"source": inject_js_content}
        )


        # Navigate to the target page
        driver.get("https://dashboard.capsolver.com/passport/login")

        # Wait for the CAPTCHA response input
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "cf-turnstile-response")))

        # Wait for the email and password fields to appear
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "email")))
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))

        # Enter email and password
        email = ""  # Replace with actual email
        password = ""  # Replace with actual password
        driver.find_element(By.NAME, "email").send_keys(email)
        driver.find_element(By.NAME, "password").send_keys(password)


        # Inject the CAPTCHA token
        driver.execute_script("""
            const captchaInput = document.querySelector('[name="cf-turnstile-response"]');
            if (captchaInput) {
                captchaInput.value = arguments[0];
                captchaInput.dispatchEvent(new Event("input", { bubbles: true }));
                captchaInput.dispatchEvent(new Event("change", { bubbles: true }));
            }
            if (window.turnstile && typeof window.tsCallback === "function") {
                window.tsCallback(arguments[0]);
            }
        """, token)

        # Wait for the submit button to be enabled
        WebDriverWait(driver, 10).until(lambda d: d.find_element(By.CSS_SELECTOR, 'form button[type="submit"]').is_enabled())

        # Click the submit button
        driver.find_element(By.CSS_SELECTOR, 'form button[type="submit"]').click()

        # Optional: Wait for the next page to load or perform further actions
        time.sleep(120)

    finally:
        # Close the browser
        # driver.quit()
        print('completed')