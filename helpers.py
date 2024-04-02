import json


class ProxyDict(dict):
    def __init__(self, name: str, change_url: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.change = change_url


def proxy_options_for_fuser():
    proxy_list = []
    with open("data/proxies.txt", "r") as f:
        for current_index, line in enumerate(f):
            proxy = line.strip().split(":")
            proxy_option = ProxyDict(
                name=line,
                change_url=f'{proxy[4]}:{proxy[5]}',
                type="http",
                host=proxy[0],
                port=proxy[1],
                username=proxy[2],
                password=proxy[3]
            )
            proxy_list.append(proxy_option)
    return proxy_list


def parse_accounts(token_pos=-1):
    accounts: list = []
    with open("data/accounts.txt", "r") as f:
        for iteration, line in enumerate(f):
            accounts.append(line.split(";")[token_pos].rstrip("\n"))
    return accounts[0]


def parse_twitters():
    accounts: list = []
    with open("data/twitters.txt", "r") as f:
        for iteration, line in enumerate(f):
            accounts.append(json.loads("["+line.split("[")[1].rstrip("\n")))
    return accounts[0]


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


def delete_account(string):
    with open('data/accounts.txt', 'r') as file:
        lines = file.readlines()
    lines = [line for line in lines if string not in line]
    with open('data/accounts.txt', 'w') as file:
        file.writelines(lines)


def delete_proxy(proxy: ProxyDict):
    with open('data/proxies.txt', 'r') as file:
        lines = file.readlines()
    lines = [line for line in lines if proxy.name not in line]
    with open('data/proxies.txt', 'w') as file:
        file.writelines(lines)


def delete_twitter(string):
    with open('data/twitters.txt', 'r') as file:
        lines = file.readlines()
    lines = [line for line in lines if string not in line]
    with open('data/twitters.txt', 'w') as file:
        file.writelines(lines)


def delete_gmail(string):
    with open('data/gmails.txt', 'r') as file:
        lines = file.readlines()
    lines = [line for line in lines if string not in line]
    with open('data/gmails.txt', 'w') as file:
        file.writelines(lines)


def parse_gmail():
    gmails = []
    with open('data/gmails.txt', 'r', encoding='utf-8') as f:
        for line in f.readlines():
            words = line.rstrip("\n").split()
            gmails.append({"gmail": words[0], "password": words[1]})
    return gmails
