from data.constants import GMAIL_LINK
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from loguru import logger
from helpers import delete_gmail


def gmail_login(driver, data):
    driver.get(GMAIL_LINK)
    try:
        logger.info("Executing gmail login : " + str(data))
        wait = WebDriverWait(driver, 10)
        sign_in_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "body > header > div > div > div > "
                                                                                 "a.button.button--medium.button--mobile-before-hero-only")))
        sign_in_button.click()
        login_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#identifierId")))
        login_input.send_keys(data["gmail"])
        next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#identifierNext > div > button")))
        next_button.click()
        password_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#password > div.aCsJod.oJeWuf > "
                                                                                 "div > div.Xb9hP > input")))
        password_input.send_keys(data["password"])
        next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#passwordNext > div > button")))
        next_button.click()
        delete_gmail(data["gmail"])
    except Exception as e:
        logger.error("Error while executing gmail : " + str(e))
