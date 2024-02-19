from helpers import parse_accounts, parse_keys
import requests
from data.constants import CLOSE_URL
from ads_power.ads_driver import AdsBrowser
from modules.discord import login_discord
from modules.rainbow import rainbow_login
from modules.molly import login_molly
from ads_power.ads_profiles import AdsProfiles
from helpers import proxy_options_for_fuser
from time import sleep


def profile_queue():
    proxy_list = proxy_options_for_fuser()
    for iteration, proxy in enumerate(proxy_list):
        if iteration < 100:
            profile_name = str(iteration)
            AdsProfiles.create_profile(profile_name, proxy)
            sleep(0.25)


def molly_queue():
    keys = parse_keys()
    proxy_list = proxy_options_for_fuser()
    serial_number = 0
    for iteration, key in enumerate(keys):
        AdsProfiles.create_profile(profile_name=str(iteration), proxy=proxy_list[iteration])
        user_id = AdsProfiles.user_ids[0]
        resp = AdsProfiles.get_ads_profile(user_id)
        ads_browser = AdsBrowser(resp)
        rainbow_login(ads_browser.driver, key=key)
        login_molly(ads_browser.driver)
        requests.get(CLOSE_URL + str(serial_number))
        ads_browser.close_driver()
        AdsProfiles.delete_profiles()


if __name__ == "__main__":
    print("Enter:\n1. To make browsers\n2. For molly\n")
    menu_options = {
        "1": profile_queue,
        "2": molly_queue
    }
    choice = input()
    if choice in menu_options:
        menu_options[choice]()
    else:
        print("Wrong input")
