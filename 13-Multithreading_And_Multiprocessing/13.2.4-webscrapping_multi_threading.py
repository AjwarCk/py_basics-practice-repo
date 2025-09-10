'''
Real-world Example: Multithreading for I/O-bound Tasks
Scenario: Web Scraping
Web scrapping often involves making numerous network requests to 
fetch web pages.
These tasks are I/O-bound because they spend a lot of time waiting 
for responses from servers.
Multithreading can significantly improve the performance by allowing 
multiple web pages to be fetched concurrently.
'''

'''
https://python.langchain.com/v0.2/docs/introduction/

https://python.langchain.com/v0.2/docs/concepts/

https://python.langchain.com/v0.2/docs/tutorials/
'''

import time
import threading
import requests
from bs4 import BeautifulSoup

urls = ['https://python.langchain.com/v0.2/docs/introduction/',

'https://python.langchain.com/v0.2/docs/concepts/',

'https://python.langchain.com/v0.2/docs/tutorials/']

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content,'html.parser')
    print(f"Fetched {len(soup.text)} characters fetched for {url}")

threads = []

start_time = time.time()

for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = time.time()

print(f"All web pages fetched! and {end_time - start_time} seconds took.")