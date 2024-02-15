from data.constants import *
from loguru import logger
from time import sleep


def login_discord(driver, token: str, is_dyno: bool):
    if is_dyno:
        sleep(3)
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(DYNO_MEME)

    else:
        driver.get(DISCORD_MEME)
    logger.info(token + " | token")
    try:
        driver.execute_script(js_code, token)
        logger.success(token + " | code executed successfully")
        sleep(2)
    except Exception as e:
        logger.error(token + " | loging in was failed" + str(e))
    logger.warning("DON'T PRESS ENTER IN THIS TERMINAL BEFORE ENDING OF VERIFYING")
