from helpers import parse_accounts, parse_keys
import requests
from modules.ads_profiles import get_ads_profile
from data.constants import CLOSE_URL
from modules.ads_driver import AdsDriver
from modules.discord import login_discord
from modules.ads_profiles import create_browser
from modules.rainbow import rainbow_login
from data.constants import MEME_FARMING


def queue(startpoint, is_dyno):
    tokens = parse_accounts()
    keys = parse_keys()
    for iteration, token in enumerate(tokens):
        resp = get_ads_profile(str(int(startpoint) + iteration))
        ads_driver = AdsDriver(resp)
        login_discord(ads_driver.driver, token, is_dyno)
        if is_dyno:
            rainbow_login(ads_driver.driver, key=keys[iteration])
            ads_driver.driver.get(MEME_FARMING)
        input()
        requests.get(CLOSE_URL + startpoint)
        ads_driver.close_driver()


if __name__ == "__main__":
    print("Enter:\n1. To make browsers\n2. Logging in discord\n3. For DYNO")
    menu_options = {
        "1": create_browser,
        "2": queue,
        "3": queue
    }
    choice = input()
    if choice in menu_options:
        if choice == "2":
            serial_n = input("Enter serial number: ")
            menu_options[choice](serial_n)
        if choice == "3":
            serial_n = input("Enter serial number: ")
            menu_options[choice](serial_n, 1)
        else:
            menu_options[choice]()
    else:
        print("Wrong input")
