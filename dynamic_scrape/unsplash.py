import requests
import os


class Unsplash:  #FIXME: pagination
    def __init__(self, search_term, per_page, max_page=1, quality="thumb"):  # constructor
        self.search_term = search_term
        self.per_page = per_page
        self.max_page = max_page
        self.quality = quality

    def set_url(self):
        """compose url with fstring"""
        return f"https://unsplash.com/napi/search?query={self.search_term}&per_page={self.per_page}&xp=&page={}"

    def make_request(self):
        url = self.set_url()
        return requests.request("GET", url)

    def get_data(self):
        self.data = self.make_request().json()

    def save_path(self, img_id):
        download_dir = 'unsplash'
        if not os.path.exists(download_dir):
            os.mkdir(download_dir)
        return f"{os.path.join(os.path.realpath(os.getcwd()), download_dir, img_id)}.jpg"

    def download(self, url, img_id):
        filepath = self.save_path(img_id)
        with open(filepath, "wb") as f:
            f.write(self.data.content)

    def run_scrapper(self):
        for page in range(1, self.max_page+1):
            self.get_data()

            for item in self.data['photos']['results']:
                img_id = item['id']
                url = item['urls'][self.quality]
                self.download(url, img_id)


scrapper = Unsplash("cars", 5)
scrapper.run_scrapper()