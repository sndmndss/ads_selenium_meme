from helpers import parse_accounts, parse_keys
import requests
from data.constants import CLOSE_URL, MOLLY_LINK
from ads_power.ads_driver import AdsBrowser
from modules.discord import login_discord
from modules.rainbow import rainbow_login
from data.constants import MEME_FARMING
from ads_power.ads_profiles import AdsProfiles
from helpers import proxy_options_for_fuser
from time import sleep
from modules.meme import meme_login


def profile_queue():
    proxy_list = proxy_options_for_fuser()
    for iteration, proxy in enumerate(proxy_list):
        profile_name = str(iteration)
        AdsProfiles.send_request(profile_name, proxy)
        sleep(0.25)
        if iteration == 100:
            break


def discord_queue(startpoint: int):
    tokens = parse_accounts()
    for iteration, token in enumerate(tokens):
        resp = AdsProfiles.get_ads_profile(str(int(startpoint) + iteration))
        ads_driver = AdsBrowser(resp)
        login_discord(ads_driver.driver, token, is_dyno=False)
        input()
        requests.get(CLOSE_URL + startpoint)
        ads_driver.close_driver()


def dyno_queue(startpoint: int):
    keys = parse_keys()
    tokens = parse_accounts()
    for iteration, token in enumerate(tokens):
        resp = AdsProfiles.get_ads_profile(str(int(startpoint) + iteration))
        ads_browser = AdsBrowser(resp)
        login_discord(ads_browser.driver, token, is_dyno=True)
        rainbow_login(ads_browser.driver, key=keys[iteration])
        ads_browser.driver.get(MEME_FARMING)
        meme_login(ads_browser.driver)
        input()
        requests.get(CLOSE_URL + startpoint)
        ads_browser.close_driver()


def molly_queue(startpoint: int):
    keys = parse_keys()
    tokens = parse_accounts()
    for iteration, token in enumerate(tokens):
        resp = AdsProfiles.get_ads_profile(str(int(startpoint) + iteration))
        ads_browser = AdsBrowser(resp)
        login_discord(ads_browser.driver, token)
        rainbow_login(ads_browser.driver, key=keys[iteration])
        ads_browser.driver.get(MOLLY_LINK)
        input()


if __name__ == "__main__":
    print("Enter:\n1. To make browsers\n2. Logging in discord\n3. For DYNO\n4. For molly")
    menu_options = {
        "1": profile_queue,
        "2": discord_queue,
        "3": dyno_queue,
        "4": molly_queue
    }
    choice = input()
    if choice in menu_options:
        if choice == "1":
            menu_options[choice]()
        elif int(choice) <= 4:
            serial_n = input("Enter serial number: ")
            menu_options[choice](serial_n)
        else:
            print("Wrong input")
    else:
        print("Wrong input")
