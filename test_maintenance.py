from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_maintenance():
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

    # Maintenance
    wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Maintenance"))
    ).click()

    # Masukkan password maintenance
    password = wait.until(
        EC.element_to_be_clickable((By.NAME, "password"))
    )
    password.send_keys("admin123")

    # Confirm
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".oxd-button--secondary")
        )
    ).click()

    # Employee Name
    employee = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".oxd-autocomplete-text-input > input")
        )
    )
    employee.click()

    # Access Records
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".oxd-topbar-body-nav-tab:nth-child(2)")
        )
    ).click()

    # Cari Ranga Akunuri
    employee = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".oxd-autocomplete-text-input > input")
        )
    )
    employee.send_keys("Ranga Akunuri")

    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(.,'Search')]")
        )
    ).click()

    # Purge Records
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".\\--parent")
        )
    ).click()

    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".oxd-dropdown-menu > li:nth-child(2)")
        )
    ).click()

    # Cari Job Title
    job = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".oxd-autocomplete-text-input > input")
        )
    )
    job.send_keys("Junior Account Assistant")

    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(.,'Search')]")
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