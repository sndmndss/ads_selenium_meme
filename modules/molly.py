from data.constants import MOLLY_LINK
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


def login_molly(driver):
    driver.get(MOLLY_LINK)
    wait = WebDriverWait(driver, 10)
    try:
        check_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Connect Wallet')]"))
        )
        check_button.click()
        sleep(1)
        rainbow_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Rainbow')]"))
        )
        rainbow_button.click()
        sleep(2)
        windows = driver.window_handles
        driver.switch_to.window(windows[-1])
        rainbow_connect = wait.until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#main > div > div > div:nth-child(1) > div > div > div > div > div "
                                  "> div:nth-child(2) > div > div > "
                                  " div._28iyjl0._28iyjl6g._28iyjl6k._28iyjl71 > div:nth-child(1) > button"))
        )
        rainbow_connect.click()
        windows = driver.window_handles
        while len(windows) == 3:
            windows = driver.window_handles
        driver.switch_to.window(windows[-1])
        sign_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Sign message')]"))
        )
        sleep(2)
        sign_button.click()
        windows = driver.window_handles
        while len(windows) == 2:
            windows = driver.window_handles
        driver.switch_to.window(windows[-1])
        sign_rainbow = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Sign')]"))
        )
        sign_rainbow.click()
        sleep(1)

    except Exception as e:
        print("Vse ploho" + str(e))
        driver.refresh()
