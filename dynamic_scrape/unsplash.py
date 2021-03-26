import requests
import os


class Unsplash:
    def __init__(self, search_term, max_page=1, per_page=10, quality="thumb"):  # constructor
        self.search_term = search_term
        self.max_page = max_page
        self.per_page = per_page
        self.quality = quality
        self.headers ={
            "Accept-Encoding": "gzip, deflate, br",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv::80.0) Gecko/20100101 Firefox/80.0"
        }

    def set_url(self, page):
        """compose url with fstring"""
        return f"https://unsplash.com/napi/search?query={self.search_term}&per_page={self.per_page}&xp=&page={page}"

    def make_request(self, page):
        url = self.set_url(page)
        response = requests.request("GET", url, headers=self.headers)
        if response.status_code == 200:
            print(f"page {page} is being crawled.")
            return response
        else:
            print(f"status code = {response.status_code}")
            raise ConnectionRefusedError

    def get_data(self, page):
        data = self.make_request(page).json()

        return data

    def save_path(self, img_id):
        download_dir = 'unsplash'
        if not os.path.exists(download_dir):
            os.mkdir(download_dir)
        return f"{os.path.join(os.path.realpath(os.getcwd()), download_dir, img_id)}.jpg"

    def download(self, img_url, img_id):
        filepath = self.save_path(img_id)
        content = requests.request("GET", img_url, headers=self.headers).content
        with open(filepath, "wb") as f:
            f.write(content)

    def run_scraper(self):
        for page in range(1, self.max_page+1):
            data = self.get_data(page)

            for item in data['photos']['results']:
                img_id = item['id']
                img_url = item['urls'][self.quality]
                self.download(img_url, img_id)


if __name__ == '__main__':
    scrapper = Unsplash("cars", 5)
    scrapper.run_scraper()