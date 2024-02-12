from ads_selenium_meme.data.constants import *
from loguru import logger
from selenium.webdriver.support.ui import WebDriverWait


def login_discord(driver, token, is_dyno: bool):
    wait = WebDriverWait(driver, 10)
    if is_dyno:
        driver.get(DYNO_MEME)
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

