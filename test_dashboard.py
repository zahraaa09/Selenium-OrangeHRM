from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dashboard():
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

    # Tunggu Dashboard
    wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//h6[normalize-space()='Dashboard']")
        )
    )

    # Buka Pending Self Review
    pending = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//p[contains(.,'Pending Self Review')]")
        )
    )
    pending.click()

    # Klik data review
    wait.until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                ".oxd-table-cell:nth-child(6) > div"
            )
        )
    ).click()

    # Buka detail review
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".bi-file-text-fill")
        )
    ).click()

    # Tunggu proses loading selesai
    wait.until(
        EC.invisibility_of_element_located(
            (By.CSS_SELECTOR, ".oxd-form-loader")
        )
    )

    # Cancel
    cancel_button = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//button[contains(.,'Cancel')]")
        )
    )

    driver.execute_script("arguments[0].click();", cancel_button)
    
    # Dashboard
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Dashboard')]")
        )
    ).click()

    # Buka widget dashboard
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".oxd-grid-item:nth-child(6) .cls-1")
        )
    ).click()

    # Kembali Dashboard
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Dashboard')]")
        )
    ).click()

    # User dropdown
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".oxd-userdropdown-name")
        )
    ).click()

    # About
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'About')]")
        )
    ).click()

    # Tutup About
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".oxd-dialog-close-button")
        )
    ).click()

    # Logout
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".oxd-userdropdown-tab")
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