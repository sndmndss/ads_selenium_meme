from data.constants import TWITTER_LINK
from loguru import logger
from helpers import delete_twitter


def login_twitter(driver, token) -> None:
    driver.get(TWITTER_LINK)
    for cookie in token:
        if cookie["domain"] == ".twitter.com":
            cookie["sameSite"] = "None"
            logger.info("Executing twitter cookies: " + str(cookie))
            driver.add_cookie(cookie)
    delete_twitter(str(token[0]))
