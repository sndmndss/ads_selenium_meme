from helpers import parse_accounts, parse_keys, parse_twitters, parse_gmail
from helpers import delete_proxy
from ads_power.ads_browser import AdsBrowser
from modules.xverse import login_xverse
from modules.rainbow import rainbow_login
from modules.molly import login_molly
from modules.rabby import rabby_login
from modules.discord import login_discord
from modules.twitter import login_twitter
from modules.gmail import gmail_login
from ads_power.ads_profiles import AdsProfiles
from helpers import proxy_options_for_fuser
from modules.stakeland import stakeland
import requests
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
    for iteration, key in enumerate(keys):
        AdsProfiles.create_profile(profile_name=str(iteration), proxy=proxy_list[iteration])
        user_id = AdsProfiles.user_ids[0]
        resp = AdsProfiles.get_ads_profile(user_id)
        ads_browser = AdsBrowser(resp)
        rainbow_login(ads_browser.driver, key=key)
        login_molly(ads_browser.driver)
        ads_browser.close_driver()
        sleep(1)
        AdsProfiles.delete_profiles()


def linea_profiles():
    keys = parse_keys()
    proxy_list = proxy_options_for_fuser()
    gmails = parse_gmail()
    for iteration, key in enumerate(keys):
        if len(proxy_list) > 1:
            proxy_index = len(proxy_list) % 2
        else:
            proxy_index = 0
        AdsProfiles.create_profile(profile_name=str(iteration), proxy=proxy_list[proxy_index])
        user_id = AdsProfiles.user_ids[0]
        resp = AdsProfiles.get_ads_profile(user_id)
        ads_browser = AdsBrowser(resp)
        rabby_login(ads_browser.driver, key)
        login_twitter(driver=ads_browser.driver)
        login_discord(ads_browser.driver)
        gmail_login(ads_browser.driver, gmails[iteration])
        while True:
            feature = input("0. To next browser\n1. To try another twitter account\n2. To try another discord account")
            if feature == "0":
                break
            elif feature == "1":
                login_twitter(ads_browser.driver)
            elif feature == "2":
                login_discord(ads_browser.driver)
        if len(proxy_list) == 1:
            requests.get(proxy_list[proxy_index].change)

        sleep(1)


def stakeland_quests():
    keys = parse_keys()
    proxy_list = proxy_options_for_fuser()
    for iteration, proxy in enumerate(proxy_list):
        AdsProfiles.create_profile(profile_name=str(iteration), proxy=proxy)
        user_id = AdsProfiles.user_ids[0]
        resp = AdsProfiles.get_ads_profile(user_id)
        ads_browser = AdsBrowser(resp)
        try:
            rainbow_login(driver=ads_browser.driver, key=keys[iteration])
            login_twitter(driver=ads_browser.driver)
            stakeland(driver=ads_browser.driver)

        except Exception:
            print("Error with twitter login")
        while True:
            feature = input("0. To next browser\n1. To try another twitter account")
            if feature == "0":
                break
            elif feature == "1":
                login_twitter(ads_browser.driver)
        delete_proxy(proxy)


if __name__ == "__main__":
    print("Enter:\n1. To make browsers\n2. For molly\n3. For LINEA\n4. Stakeland")
    menu_options = {
        "1": profile_queue,
        "2": molly_queue,
        "3": linea_profiles,
        "4": stakeland_quests
    }
    choice = input()
    if choice in menu_options:
        menu_options[choice]()
    else:
        print("Wrong input")
