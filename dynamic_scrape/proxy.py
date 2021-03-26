import requests
from bs4 import BeautifulSoup
from random import choice


def get_proxies():
    proxy_url = "https://github.com/clarketm/proxy-list/blob/master/proxy-list-raw.txt"
    r = requests.get(proxy_url)
    soup = BeautifulSoup(r.content, "html.parser").select('td.blob-code.blob-code-inner')
    proxies = [proxy.text for proxy in soup]

    return proxies


def get_random_proxy(proxies):
    return {"https": choice(proxies)}


proxies = get_proxies()


def get_working_proxies():
    working_proxies = list()
    for i in range(30):
        proxy = get_random_proxy(proxies)
        print(f"using {proxy}...")
        try:
            r = requests.get("https://www.google.com", proxies=proxy, timeout=2)
            if r.status_code == 200:
                working_proxies.append(proxy)
        except:
            pass
    return working_proxies

url = "https://pexels.com"
proxy = choice(get_working_proxies())

requests.get(url, proxies=proxy)