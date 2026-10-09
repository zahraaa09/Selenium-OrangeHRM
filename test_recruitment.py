from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_recruitment():
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

    # Buka Recruitment
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[normalize-space()='Recruitment']")
        )
    ).click()

    # Delete candidate pada baris pertama
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".oxd-table-card:nth-child(1) .oxd-icon-button:nth-child(2)")
        )
    ).click()

    # Konfirmasi delete
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(.,'Yes, Delete')]")
        )
    ).click()

    # Klik kandidat pada baris kedua
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".oxd-table-card:nth-child(2) .oxd-icon-button:nth-child(1)")
        )
    ).click()

    # Buka Vacancies
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//li[contains(.,'Vacancies')]")
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