from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_performance():
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

    # Buka Performance
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Performance')]")
        )
    ).click()

    # Configure > KPIs
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(.,'Configure')]")
        )
    ).click()

    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".oxd-dropdown-menu > li:nth-child(1)")
        )
    ).click()

    # Klik tombol edit pada data terakhir
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".oxd-table-card:nth-child(12) .oxd-icon-button:nth-child(1)")
        )
    ).click()

        # Tunggu form selesai loading
    wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".oxd-select-text-input")
        )
    )

    # Tunggu sebentar sampai loader selesai
    import time
    time.sleep(3)

    
    # Configure > Trackers
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//span[contains(.,'Configure')]")
        )
    ).click()

    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Trackers')]")
        )
    ).click()

    # Manage Reviews > My Reviews
    manage_reviews = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[contains(.,'Manage Reviews')]")
        )
    )

    driver.execute_script("arguments[0].click();", manage_reviews)

    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'My Reviews')]")
        )
    ).click()

    # Manage Reviews > Employee Reviews
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".--visited > .oxd-topbar-body-nav-tab-item")
        )
    ).click()

    wait.until(
        EC.element_to_be_clickable(
            (By.LINK_TEXT, "Employee Reviews")
        )
    ).click()

    # My Trackers
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".oxd-topbar-body-nav-tab:nth-child(3)")
        )
    ).click()

    # View
    wait.until(
        EC.element_to_be_clickable(
            (By.NAME, "view")
        )
    ).click()

    # Employee Trackers
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//a[contains(.,'Employee Trackers')]")
        )
    ).click()

    # View
    wait.until(
        EC.element_to_be_clickable(
            (By.NAME, "view")
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