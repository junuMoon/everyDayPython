import requests


def get_proxy_list():
    proxy_list = requests.get('https://cdn.jsdelivr.net/gh/clarketm/proxy-list@master/proxy-list-raw.txt').text.split('\n')
    return proxy_list


def get_working_proxies(proxy_list):
    working_proxies = list()
    for proxy in proxy_list:
        if proxy != '':
            try:
                r = requests.get("https://google.com", proxies={'https': proxy}, timeout=2)
                if r.status_code == 200:
                    print(f"{proxy} is working!")
                    working_proxies.append(proxy)
            except:
                print(f"{proxy} fails.")
                pass
    return working_proxies


print(get_working_proxies(get_proxy_list()))