from data.constants import *
from loguru import logger
from helpers import delete_discord


def login_discord(driver, token: str, is_dyno=0):
    if is_dyno:
        driver.get(DYNO_MEME)
    else:
        driver.get(DISCORD)
    logger.info(token + " | token")
    try:
        driver.execute_script(js_code, token)
        logger.success(token + " | code executed successfully")
        delete_discord(token)
    except Exception as e:
        logger.error(token + " | loging in was failed" + str(e))
    logger.warning("DON'T PRESS ENTER IN THIS TERMINAL BEFORE ENDING OF VERIFYING")
