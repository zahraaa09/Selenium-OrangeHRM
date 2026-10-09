from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_leave():
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

    # Buka Leave
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[normalize-space()='Leave']")
        )
    ).click()

    # Assign Leave
    wait.until(
        EC.element_to_be_clickable(
            (By.LINK_TEXT, "Assign Leave")
        )
    ).click()

    # Employee Name
    employee = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".oxd-autocomplete-text-input > input")
        )
    )
    employee.send_keys("Ravi M B")

    # Pilih employee
    employee_option = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'oxd-autocomplete-option')]")
        )
    )
    employee_option.click()

    # From Date
    wait.until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                ".oxd-grid-item:nth-child(1) .oxd-date-wrapper .oxd-icon"
            )
        )
    ).click()

    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".oxd-calendar-date-wrapper:nth-child(5) > .oxd-calendar-date")
        )
    ).click()

    # To Date
    wait.until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                ".oxd-grid-item:nth-child(2) .oxd-date-wrapper .oxd-icon"
            )
        )
    ).click()

    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".oxd-calendar-date-wrapper:nth-child(6) > .oxd-calendar-date")
        )
    ).click()

    # Leave Type
    leave_type = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//label[normalize-space()='Leave Type']/ancestor::div[contains(@class,'oxd-input-group')]//i"
            )
        )
    )
    leave_type.click()

    # Assign
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(., 'Assign')]")
        )
    ).click()

    # Logout
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".oxd-userdropdown-name")
        )
    ).click()

    wait.until(
        EC.element_to_be_clickable(
            (By.LINK_TEXT, "Logout")
        )
    ).click()

    wait.until(
        EC.url_contains("/web/index.php/auth/login")
    )

    driver.quit()