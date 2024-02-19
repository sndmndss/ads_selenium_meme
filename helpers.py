from random import randint
from selenium.webdriver.common.action_chains import ActionChains


def proxy_options_for_fuser():
    proxy_list = []
    with open("data/proxies.txt", "r") as f:
        for current_index, line in enumerate(f):
            proxy = line.strip().split(":")
            proxy_option = {
                    "type": "http",
                    "host": proxy[0],
                    "port": proxy[1],
                    "username": proxy[2],
                    "password": proxy[3]
                }
            proxy_list.append(proxy_option)
    return proxy_list


def parse_accounts():
    accounts: list = []
    with open("data/accounts.txt", "r") as f:
        for iteration, line in enumerate(f):
            accounts.append(line.split(";")[-1].rstrip("\n"))
    return accounts


def parse_keys():
    keys = []
    with open("data/keys.txt", "r") as f:
        for line in f:
            keys.append(line.rstrip("\n"))
    return keys


def delete_key(string):
    with open('data/keys.txt', 'r') as file:
        lines = file.readlines()
    lines = [line for line in lines if string not in line]
    with open('data/keys.txt', 'w') as file:
        file.writelines(lines)


def delete_discord(string):
    with open('data/accounts.txt', 'r') as file:
        lines = file.readlines()
    lines = [line for line in lines if string not in line]
    with open('data/accounts.txt', 'w') as file:
        file.writelines(lines)


def randomize_click(button, driver):
    actions = ActionChains(driver)
    button_size = button.size
    button_width = button_size['width']
    button_height = button_size['height']
    offset_x = randint(0, button_width)
    offset_y = randint(0, button_height)
    actions.move_to_element_with_offset(button, offset_x, offset_y).click().perform()
