from data.constants import *
from time import sleep
from fake_useragent import UserAgent
import requests
from loguru import logger
from helpers import proxy_options_for_fuser


def send_request(profile_name, country, timezone, proxy, group_id):

    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "name": profile_name,
        "country": country,
        "timezone": timezone,
        "group_id": str(group_id),
        "open_urls": [MEME_FARMING,],
        "fingerprint_config": {
            "automatic_timezone": "1",
            "language_switch": "1",
            "ua": UserAgent(os=["windows", "macos"]).random
        },
        "user_proxy_config": {
            "proxy_soft": "other",
            "proxy_type": proxy['type'],
            "proxy_host": proxy['host'],
            "proxy_port": proxy['port'],
            "proxy_user": proxy['username'],
            "proxy_password": proxy['password']
        }
    }
    response = requests.post(f"{API_URL}/api/v1/user/create", headers=headers, json=data)
    if response.status_code == 200:
        logger.success("Successfully created")
        logger.info(response.json())
    else:
        logger.error("There was some trouble")
        logger.info(response.json())


def create_browser():
    proxy_list = proxy_options_for_fuser()
    browser_number = 0
    for iteration, proxy in enumerate(proxy_list):
        profile_name = str(iteration)
        country = "US"
        timezone = "GMT-5"
        group_id = 0
        send_request(profile_name, country, timezone, proxy, group_id)
        browser_number += 1
        sleep(1)
        if browser_number == 100:
            break


def get_ads_profile(startpoint):
    resp = requests.get(OPEN_URL + startpoint).json()
    logger.info(f"{resp['msg']}\n Make sure that serial number exists\nIf you sure, re-roll user agent in this profile")
    return resp
