from loguru import logger

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from data.css_selectors import (RAINBOW_INPUT_CSS_SELECTOR,
                                RAINBOW_BUTTON_CSS_SELECTOR,
                                RAINBOW_PASSWORD_1,
                                RAINBOW_PASSWORD_2,
                                RAINBOW_BUTTON_2_CSS_SELECTOR)


def proxy_options_for_fuser():
    proxy_list = []
    with open("data/proxies.txt", "r") as f:
        for current_index, line in enumerate(f):
            proxy = line.strip().split(":")
            proxy_option = {
                    "type": "http",
                    "host": proxy[0],
                    "port": proxy[1],
                    "username": proxy[2],
                    "password": proxy[3]
                }
            proxy_list.append(proxy_option)
    return proxy_list


def parse_accounts():
    accounts: list = []
    with open("data/accounts.txt", "r") as f:
        for iteration, line in enumerate(f):
            accounts.append(line.split(";")[-1].rstrip("\n"))
    return accounts


def parse_keys():
    keys = []
    with open("data/keys.txt", "r") as f:
        for line in f:
            keys.append(line.rstrip("\n"))
    return keys


def wait_for_tab_to_load(driver, window_handle, timeout=50):
    driver.switch_to.window(window_handle)
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )


def rainbow_fill(driver, key, password="8901324567Ww"):
    logger.info(f"{key} | private key in progress")
    wait = WebDriverWait(driver, 10)
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
