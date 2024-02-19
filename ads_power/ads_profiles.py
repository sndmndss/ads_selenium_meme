from data.constants import *
from fake_useragent import UserAgent
import requests
from loguru import logger


class AdsProfiles:
    country = "US"
    timezone = "GMT-5"
    group_id = 0
    user_ids = []

    @classmethod
    def create_profile(cls, profile_name, proxy):
        data = {
            "name": profile_name,
            "country": cls.country,
            "timezone": cls.timezone,
            "group_id": str(cls.group_id),
            "fingerprint_config": {
                "automatic_timezone": "1",
                "language_switch": "1",
                "ua": UserAgent(os=["windows"], browsers=["chrome", "edge", "firefox", "safari"]).random
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
        response = requests.post(f"{API_URL}/api/v1/user/create", json=data)
        if response.status_code == 200:
            logger.success("Successfully posted")
            logger.info(response.json())
            cls.user_ids.append(response.json()["data"]["id"])
        else:
            logger.error("There was some trouble")
            logger.info(response.json())

    @classmethod
    def delete_profiles(cls):
        data = {
            "user_ids": cls.user_ids
        }
        response = requests.post(f"{API_URL}/api/v1/user/delete", json=data)
        cls.user_ids = []
        if response.status_code == 200:
            logger.success("Successfully posted")
            logger.info(response.json())
        else:
            logger.error("There was some trouble")
            logger.info(response.json())

    @classmethod
    def get_ads_profile(cls, startpoint):
        resp = requests.get(OPEN_URL_ID + startpoint).json()
        logger.info(f"{resp['msg']}\n Make sure that serial number exists\nIf you sure, re-roll user agent in this profile")
        return resp
