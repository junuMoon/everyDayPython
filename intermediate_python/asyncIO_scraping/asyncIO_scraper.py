import asyncio
import timeit
import requests
from concurrent.futures import ThreadPoolExecutor
import threading
from bs4 import BeautifulSoup

start_tm = timeit.default_timer()
urls = ['http://daum.net', 'https://naver.com', 'http://mlbpark.donga.com', 'https://tistory.com']

async def fetch(url, executor):
    print(f'Thread Name: {threading.current_thread().getName()} Url: {url}')
    response = await loop.run_in_executor(executor, requests.get, url)
    if response.ok:
        print(f'{url} request success')
    
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.find('title').text
    
    return {url: title}

async def main():
    executor = ThreadPoolExecutor(max_workers=10)
    futures = [
        asyncio.ensure_future(fetch(url, executor)) for url in urls
    ]
    
    result = await asyncio.gather(*futures)  # yield

    print()
    print(f'Result: {result}')
    
    
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    duration = timeit.default_timer() - start_tm
    print(f'Run time: {duration}')