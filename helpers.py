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


