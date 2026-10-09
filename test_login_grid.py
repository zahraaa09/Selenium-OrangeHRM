from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_orangehrm():
    import os

    options = Options()
    firefox_binary = os.getenv("FIREFOX_BINARY")

    if firefox_binary:
        options.binary_location = firefox_binary

    driver = webdriver.Remote(
        command_executor="http://localhost:4444",
        options=options
    )

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    wait = WebDriverWait(driver, 30)

    username = wait.until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username.click()
    username.send_keys("Admin")

    password = wait.until(
        EC.presence_of_element_located((By.NAME, "password"))
    )
    password.click()
    password.send_keys("admin123")

    login_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-button"))
    )
    login_button.click()

    # Logout
    profile = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//img[@alt='profile picture']"))
    )
    profile.click()

    logout = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Logout']"))
    )
    logout.click()

    wait.until(
        EC.url_contains("/web/index.php/auth/login")
    )

    driver.quit()