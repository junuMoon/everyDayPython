import requests

url = "https://unsplash.com/napi/search?query=dog&per_page=20&xp=&page=0"

r = requests.get(url)

data = r.json()

file_path = './images/'
for item in data['photos']['results']:
    name = item['id']
    url = item['urls']['thumb']
    with open(f"{file_path}{name}.jpg", "wb") as f:
        f.write(requests.get(url).content)
