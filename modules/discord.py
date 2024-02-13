from data.constants import *
from loguru import logger


def login_discord(driver, token: str, is_dyno: bool):
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