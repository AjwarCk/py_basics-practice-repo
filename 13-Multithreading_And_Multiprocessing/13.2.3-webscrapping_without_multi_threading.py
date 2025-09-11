## Webscrapping without multi-threading

'''
https://python.langchain.com/v0.2/docs/introduction/

https://python.langchain.com/v0.2/docs/concepts/

https://python.langchain.com/v0.2/docs/tutorials/
'''

import time
import requests
from bs4 import BeautifulSoup

urls = ['https://python.langchain.com/v0.2/docs/introduction/',

'https://python.langchain.com/v0.2/docs/concepts/',

'https://python.langchain.com/v0.2/docs/tutorials/']

def fetch_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(f"Fetched {len(soup.text)} characters from {url}")

start_time = time.time()

for url in urls:
    fetch_content(url)

end_time = time.time()

print(f"All web pages fetched and {end_time - start_time} seconds took.")
