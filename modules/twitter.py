from data.constants import TWITTER_LINK
from loguru import logger
from helpers import delete_twitter
from helpers import parse_accounts


def login_twitter(driver) -> None:
    token = parse_accounts()
    driver.get(TWITTER_LINK)
    static_cookie = token
    for cookie_name in token:
        try:
            driver.delete_cookie(cookie_name)
        except Exception:
            pass
    for cookie in token:
        if cookie["domain"] == ".twitter.com":
            cookie["sameSite"] = "None"
            logger.info("Executing twitter cookies: " + str(cookie))
            driver.add_cookie(cookie)
    delete_twitter(str(static_cookie[2]["value"]))
