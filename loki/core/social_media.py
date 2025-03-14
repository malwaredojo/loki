#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from core.colours import *
import time

def create_social_accounts(person_data):
    # Initialize Selenium WebDriver (Chrome)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    try:
        # Example: Create a Facebook account (simplified)
        print(f"{info} Creating Facebook account for {person_data['name']}...")
        driver.get("https://www.facebook.com/r.php")
        time.sleep(2)  # Wait for page load

        # Fill in form (example fields; adjust selectors as needed)
        driver.find_element_by_name("firstname").send_keys(person_data['name'].split()[0])
        driver.find_element_by_name("lastname").send_keys(person_data['name'].split()[-1])
        driver.find_element_by_name("reg_email__").send_keys(person_data['email'])
        driver.find_element_by_name("reg_passwd__").send_keys("SecurePass123!")
        driver.find_element_by_name("birthday_day").send_keys(person_data['birthday'].split('/')[0])
        driver.find_element_by_name("birthday_month").send_keys(person_data['birthday'].split('/')[1])
        driver.find_element_by_name("birthday_year").send_keys(person_data['birthday'].split('/')[2])
        driver.find_element_by_css_selector(f"input[value='{person_data['gender'].lower()[0]}']").click()
        driver.find_element_by_name("websubmit").click()
        
        time.sleep(5)  # Wait for submission
        print(f"{good} Facebook account created for {person_data['name']}")

        # Placeholder for Instagram, TikTok (similar logic)
        print(f"{info} Instagram and TikTok account creation TBD...")

    except Exception as e:
        print(f"{bad} Failed to create social media accounts: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    # Test data
    test_data = {
        "name": "John Doe",
        "gender": "male",
        "birthday": "01/01/1990",
        "street": "123 Fake St",
        "telephone": "123-456-7890",
        "email": "john.doe@example.com",
        "occupation": "Engineer",
        "country": "US"
    }
    create_social_accounts(test_data)
