from data.constants import *
from loguru import logger
from helpers import delete_key
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from data.css_selectors import (RAINBOW_INPUT_CSS_SELECTOR,
                                RAINBOW_BUTTON_CSS_SELECTOR,
                                RAINBOW_PASSWORD_1,
                                RAINBOW_PASSWORD_2,
                                RAINBOW_BUTTON_2_CSS_SELECTOR)
import time


def rainbow_login(driver, key: str):
    start_time = time.time()
    found = False
    while not found:
        if time.time() - start_time > 30:
            break
        window_handles = driver.window_handles
        for handle in window_handles:
            driver.switch_to.window(handle)
            if driver.title == "Rainbow Wallet":
                found = True
                break
    driver.get(RAINBOW_LINK)
    _rainbow_fill(driver, key)


def _rainbow_fill(driver, key, password="8901324567Ww"):
    logger.info(f"{key} | private key in progress")
    wait = WebDriverWait(driver, 10)
    try:
        rainbow_key_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                                                                        RAINBOW_INPUT_CSS_SELECTOR)))
        rainbow_key_input.send_keys(key)
        rainbow_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, RAINBOW_BUTTON_CSS_SELECTOR)))
        rainbow_button.click()
        rainbow_password_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, RAINBOW_PASSWORD_1)))
        rainbow_password_input.send_keys(password)
        rainbow_password_confirm = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, RAINBOW_PASSWORD_2)))
        rainbow_password_confirm.send_keys(password)
        rainbow_password_confirm_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                                 RAINBOW_BUTTON_2_CSS_SELECTOR)))
        rainbow_password_confirm_button.click()
        logger.info(f"{key} | private key done")
        delete_key(key)
    except Exception as e:
        logger.error("Something went wrong " + str(e))
