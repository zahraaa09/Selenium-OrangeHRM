from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_admin():
    options = Options()
    options.binary_location = r"C:\Program Files\Mozilla Firefox ESR\firefox.exe"

    driver = webdriver.Firefox(options=options)
    wait = WebDriverWait(driver, 30)

    driver.get(
        "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    )

    # Login
    wait.until(
        EC.presence_of_element_located((By.NAME, "username"))
    ).send_keys("Admin")

    wait.until(
        EC.presence_of_element_located((By.NAME, "password"))
    ).send_keys("admin123")

    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-button"))
    ).click()

    # Buka Admin
    wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Admin"))
    ).click()

    # Klik Add
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(.,'Add')]")
        )
    ).click()

    # Employee Name
    employee = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".oxd-autocomplete-text-input > input")
        )
    )
    employee.send_keys("Ritesh Varun Sharma")

    # Username
    username = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'oxd-input-group')][.//label[text()='Username']]//input")
        )
    )
    username.send_keys("Riteshz")

    # Save
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(.,'Save')]")
        )
    ).click()

    # Logout
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".oxd-userdropdown-name")
        )
    ).click()

    wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))
    ).click()

    wait.until(EC.url_contains("/web/index.php/auth/login"))

    driver.quit()