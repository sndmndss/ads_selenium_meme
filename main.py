from helpers import parse_accounts, parse_keys
import requests
from data.constants import CLOSE_URL
from modules.ads_driver import AdsDriver
from modules.discord import login_discord
from modules.rainbow import rainbow_login
from data.constants import MEME_FARMING
from modules.ads_profiles import AdsProfiles
from helpers import proxy_options_for_fuser
from time import sleep


def profile_queue():
    proxy_list = proxy_options_for_fuser()
    for iteration, proxy in enumerate(proxy_list):
        profile_name = str(iteration)
        AdsProfiles.send_request(profile_name, proxy)
        sleep(0.19)
        if iteration == 100:
            break


def discord_queue(startpoint=0):
    tokens = parse_accounts()
    for iteration, token in enumerate(tokens):
        resp = AdsProfiles.get_ads_profile(str(int(startpoint) + iteration))
        ads_driver = AdsDriver(resp)
        login_discord(ads_driver.driver, token, is_dyno=False)
        input()
        requests.get(CLOSE_URL + startpoint)
        ads_driver.close_driver()


def dyno_queue(startpoint):
    keys = parse_keys()
    tokens = parse_accounts()
    for iteration, token in enumerate(tokens):
        resp = AdsProfiles.get_ads_profile(str(int(startpoint) + iteration))
        ads_driver = AdsDriver(resp)
        login_discord(ads_driver.driver, token, is_dyno=True)
        rainbow_login(ads_driver.driver, key=keys[iteration])
        ads_driver.driver.get(MEME_FARMING)
        input()
        requests.get(CLOSE_URL + startpoint)
        ads_driver.close_driver()


if __name__ == "__main__":
    print("Enter:\n1. To make browsers\n2. Logging in discord\n3. For DYNO")
    menu_options = {
        "1": profile_queue,
        "2": discord_queue,
        "3": dyno_queue
    }
    choice = input()
    if choice in menu_options:
        if choice == "1":
            menu_options[choice]()
        if choice == "2":
            serial_n = input("Enter serial number: ")
            menu_options[choice](serial_n)
        if choice == "3":
            serial_n = input("Enter serial number: ")
            menu_options[choice](serial_n)
        else:
            menu_options[choice]()
    else:
        print("Wrong input")
