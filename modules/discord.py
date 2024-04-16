from data.constants import *
from loguru import logger
from helpers import delete_account, parse_accounts


def login_discord(driver, is_dyno=0):
    token = parse_accounts()
    try:
        driver.delete_cookie("token")
    except Exception:
        pass
    if is_dyno:
        driver.get(DYNO_MEME)
    else:
        driver.get(DISCORD)
    logger.info(token + " | token")
    try:
        driver.execute_script(js_code_discord, token)
        logger.success(token + " | code executed successfully")
        delete_account(token)
    except Exception as e:
        logger.error(token + " | loging in was failed" + str(e))
    logger.warning("DON'T PRESS ENTER IN THIS TERMINAL BEFORE ENDING OF VERIFYING")
