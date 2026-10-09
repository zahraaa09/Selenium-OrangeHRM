from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_buzz():
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

    # Buzz
    buzz = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//span[normalize-space()='Buzz']")
        )
    )

    driver.execute_script("arguments[0].click();", buzz)

    # Edit post pertama
    wait.until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                ".oxd-grid-item:nth-child(1) > .oxd-sheet "
                "> .orangehrm-buzz-post .oxd-icon"
            )
        )
    ).click()

    # Pilih Edit Post
    wait.until(
        EC.element_to_be_clickable(
            (
                By.CSS_SELECTOR,
                ".orangehrm-buzz-post-header-config-item:nth-child(2) > .oxd-text"
            )
        )
    ).click()

    # Edit teks post
    text_area = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "textarea.oxd-buzz-post-input")
        )
    )

    driver.execute_script(
        "arguments[0].value = 'Testing Buzz Post dengan Selenium WebDriver';"
        "arguments[0].dispatchEvent(new Event('input', {bubbles: true}));",
        text_area
    )

    # Save
    wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".oxd-form-actions > .oxd-button")
        )
    ).click()

    # Tunggu dialog edit tertutup
    wait.until(
        EC.invisibility_of_element_located(
            (By.CSS_SELECTOR, ".oxd-dialog-container-default")
        )
    )

    # Like
    heart = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "path.orangehrm-heart-icon-path")
        )
    )[0]

    driver.execute_script(
        """
        var svg = arguments[0].parentElement;
        svg.dispatchEvent(new MouseEvent('click', {
            bubbles: true,
            cancelable: true,
            view: window
        }));
        """,
        heart
    )

    # Most Liked Posts
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(.,'Most Liked Posts')]")
        )
    ).click()

    # Most Commented Posts
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[contains(.,'Most Commented Posts')]")
        )
    ).click()

    # Scroll
    driver.execute_script("window.scrollTo(0,100)")

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