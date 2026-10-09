from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_time():
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

    # Buka Time
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[normalize-space()='Time']")
        )
    ).click()

    # Klik tombol pada baris pertama
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".oxd-table-card:nth-child(1) .oxd-button")
        )
    ).click()

    # Klik Edit
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(.,'Edit')]")
        )
    ).click()

    # Project
    project = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".oxd-autocomplete-text-input > input")
        )
    )
    project.send_keys("Apache Software Foundation - ASF - Phase 1")

    # Pilih project dari autocomplete
    project_option = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class,'oxd-autocomplete-option')]")
        )
    )
    project_option.click()

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
        EC.element_to_be_clickable(
            (By.LINK_TEXT, "Logout")
        )
    ).click()

    wait.until(
        EC.url_contains("/web/index.php/auth/login")
    )

    driver.quit()