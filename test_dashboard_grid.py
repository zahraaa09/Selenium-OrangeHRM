from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


def test_dashboard():
    options = Options()
    firefox_binary = os.getenv("FIREFOX_BINARY")

    if firefox_binary:
        options.binary_location = firefox_binary
    elif os.path.exists(r"C:\Program Files\Mozilla Firefox ESR\firefox.exe"):
        options.binary_location = r"C:\Program Files\Mozilla Firefox ESR\firefox.exe"

    driver = webdriver.Remote(
        command_executor="http://127.0.0.1:4444",
        options=options
    )

    try:
        wait = WebDriverWait(driver, 30)

        driver.get(
            "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        )

        wait.until(
            EC.visibility_of_element_located((By.NAME, "username"))
        ).send_keys("Admin")

        wait.until(
            EC.visibility_of_element_located((By.NAME, "password"))
        ).send_keys("admin123")

        wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-button"))
        ).click()

        wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//h6[normalize-space()='Dashboard']")
            )
        )

    finally:
        driver.quit()

