from ads_selenium_meme.helpers import parse_accounts
import requests
from ads_selenium_meme.modules import get_ads_profile
from ads_selenium_meme.data import CLOSE_URL
from ads_selenium_meme.modules.ads_driver import AdsDriver
from ads_selenium_meme.modules.discord import login_discord
from ads_selenium_meme.modules import create_browser


def discord_queue(startpoint, is_dyno):
    tokens = parse_accounts()
    for iteration, token in enumerate(tokens):
        resp = get_ads_profile(str(int(startpoint) + iteration))
        ads_driver = AdsDriver(resp)
        login_discord(ads_driver.driver, token, is_dyno)
        requests.get(CLOSE_URL + startpoint)
        ads_driver.close_driver()


if __name__ == "__main__":
    print("Enter:\n1. To make browsers\n2. Logging in discord\n3. For DYNO")
    menu_options = {
        "1": create_browser,
        "2": discord_queue,
        "3": discord_queue
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
