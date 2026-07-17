from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Launch Chrome
driver = webdriver.Chrome()

# Maximize browser
driver.maximize_window()

# Open Contact Page
driver.get("https://example.com/contact")

try:
    # Fill Contact Form
    driver.find_element(By.ID, "name").send_keys("John Doe")
    driver.find_element(By.ID, "email").send_keys("john@example.com")
    driver.find_element(By.ID, "subject").send_keys("Inquiry")
    driver.find_element(By.ID, "message").send_keys("This is a test message.")

    # Click Submit button
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # Wait until success message appears
    success = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".alert-success")
        )
    )

    # Verify Success Message
    expected = "Your message has been sent successfully."
    actual = success.text

    if actual == expected:
        print("✅ Test Passed")
        print("Success Message:", actual)
    else:
        print("❌ Test Failed")
        print("Expected:", expected)
        print("Actual:", actual)

except Exception as e:
    print("Error:", e)

finally:
    driver.quit()