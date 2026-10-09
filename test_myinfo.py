from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_myinfo():
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


    # DEBUG
    time.sleep(5)
    print("URL SETELAH LOGIN:", driver.current_url)
    print("TITLE:", driver.title)

    # Buka My Info
    my_info = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//a[contains(.,'My Info')]")
        )
    )

    driver.execute_script("arguments[0].click();", my_info)

    wait.until(
        EC.url_contains("/pim/viewPersonalDetails")
    )

    # Buka Contact Details
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Contact Details')]")
        )
    ).click()

    # Emergency Contacts
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Emergency Contacts')]")
        )
    ).click()

    # Dependents
    dependents = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[contains(normalize-space(),'Dependents')]")
        )
    )
    driver.execute_script("arguments[0].click();", dependents)

    # Immigration
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Immigration')]")
        )
    ).click()

    # Job
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Job')]")
        )
    ).click()

    # Salary
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Salary')]")
        )
    ).click()

    # Report-to
    report_to = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[contains(normalize-space(),'Report-to')]")
        )
    )
    driver.execute_script("arguments[0].click();", report_to)

    # Qualifications
    qualifications = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[contains(normalize-space(),'Qualifications')]")
        )
    )
    driver.execute_script("arguments[0].click();", qualifications)

    # Memberships
    memberships = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//*[contains(normalize-space(),'Memberships')]")
        )
    )
    driver.execute_script("arguments[0].click();", memberships)

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