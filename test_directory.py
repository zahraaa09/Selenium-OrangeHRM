from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_directory():
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

    # Buka Directory
    wait.until(
        EC.element_to_be_clickable(
            (By.LINK_TEXT, "Directory")
        )
    ).click()

    # Klik card ke-6
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".oxd-grid-item:nth-child(6) > .oxd-sheet")
        )
    ).click()

    # Buka sidebar
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".orangehrm-corporate-directory-sidebar .oxd-sheet")
        )
    ).click()

    # Tutup sidebar
    close_icon = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".orangehrm-corporate-directory-sidebar .orangehrm-directory-card-top > .oxd-icon")
        )
    )

    driver.execute_script("arguments[0].click();", close_icon)

    # Klik card ke-3
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".oxd-grid-item:nth-child(3) .orangehrm-directory-card-header")
        )
    ).click()

    # Tutup sidebar
    close_icon = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".orangehrm-corporate-directory-sidebar .orangehrm-directory-card-top > .oxd-icon")
        )
    )

    driver.execute_script("arguments[0].click();", close_icon)

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