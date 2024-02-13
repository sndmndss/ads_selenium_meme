from data.constants import *
from loguru import logger
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def login_discord(driver, token: str, is_dyno: bool):
    if is_dyno:
        driver.get(DYNO_MEME)
        window_handles = driver.window_handles
        _wait_for_tab_to_load(driver, window_handles[2])
        _open_rainbow(driver)
        _wait_for_tab_to_load(driver, window_handles[1])
        driver.switch_to.window(window_handles[1])
    else:
        driver.get(DISCORD_MEME)
    logger.info(token + " | token")
    try:
        driver.execute_script(js_code, token)
        logger.success(token + " | code executed successfully")
    except Exception as e:
        logger.error(token + " | loging in was failed" + str(e))
    logger.warning("DON'T PRESS ENTER IN THIS TERMINAL BEFORE ENDING OF VERIFYING")
    input()


def _open_rainbow(driver):
    driver.get(RAINBOW_LINK)


def _wait_for_tab_to_load(driver, window_handle, timeout=50):
    driver.switch_to.window(window_handle)
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
