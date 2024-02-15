from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep


def meme_login(driver):
    wait = WebDriverWait(driver, 10)
    check_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'CHECK PROGRESS WITH WALLET')]"))
    )
    check_button.click()
    sleep(0.5)
    rainbow_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Rainbow')]"))
    )
    rainbow_button.click()
    sleep(3)
    windows = driver.window_handles
    driver.switch_to.window(windows[-1])
    rainbow_connect = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#main > div > div > div:nth-child(1) > div > div > div > div > div "
                                              "> div:nth-child(2) > div > div > "
                                              " div._28iyjl0._28iyjl6g._28iyjl6k._28iyjl71 > div:nth-child(1) > button"))
    )
    rainbow_connect.click()
    sleep(4)
    windows = driver.window_handles
    driver.switch_to.window(windows[-1])
    rainbow_sign = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#main > div > div > div:nth-child(1) > div > div > div > div > "
                                                     "div > div._28iyjl0._28iyjlhe._28iyjldt._28iyjlf0._28iyjlg7._28iyjl6g._28iyjl6k._28iyjl7a "
                                                     "> div._28iyjl0._28iyjl6g._28iyjl6j._28iyjl82._28iyjl74 > div:nth-child(2) > button"))
    )
    rainbow_sign.click()
    windows = driver.window_handles
    driver.switch_to.window(windows[1])
