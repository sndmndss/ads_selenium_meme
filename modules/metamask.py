import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def login_metamask(driver, private_key):
    start_time = time.time()
    found = False
    while not found:
        if time.time() - start_time > 30:
            break
        window_handles = driver.window_handles
        for handle in window_handles:
            driver.switch_to.window(handle)
            if driver.title == "MetaMask":
                found = True
                break

    _fill_metamask(driver, private_key)


def _fill_metamask(driver, private_key, password=8901324567):
    wait = WebDriverWait(driver, 10)
    time.sleep(2)
    driver.execute_script("document.querySelector('[data-testid=\"onboarding-terms-checkbox\"]').click();")
    driver.execute_script("document.querySelector('[data-testid=\"onboarding-create-wallet\"]').click();")
    driver.execute_script("document.querySelector('[data-testid=\"metametrics-i-agree\"]').click();")
    time.sleep(1)
    password_field = driver.find_element(By.CSS_SELECTOR, '[data-testid="create-password-new"]')
    driver.execute_script("arguments[0].setAttribute('value', '13241231');", password_field)
    time.sleep(1)
    password_field = driver.find_element(By.CSS_SELECTOR, '[data-testid="create-password-confirm"]')
    driver.execute_script("arguments[0].setAttribute('value', '13241231');", password_field)
    driver.execute_script("document.querySelector('[data-testid=\"create-password-terms\"]').click();")
    driver.execute_script("document.querySelector('[data-testid=\"create-password-wallet\"]').click();")
