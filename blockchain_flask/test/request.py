import requests
import pprint

host = 'http://localhost:5000'
# path = '/mine'
# path = '/chain'
# params = {}
path = '/transactions/new'
params = {
    'sender': '98a8374a665945e895a7b1c3cb8ba630',
    'recipient': 'new',
    'amount': 5
}

url = host+path
# response = requests.get(url, json=params)
response = requests.post(url, json=params)
pprint.pprint(response.content)