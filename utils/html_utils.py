import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def all_sub_url(url):
    sub_urls = []
    response = []
    try:
        response = requests.get(url)
    except requests.exceptions.ConnectTimeout:
        sub_urls = [url]
    except requests.exceptions.ConnectionError:
        sub_urls = [url]
    if response and response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')
        sub_urls = [urljoin(url, link.get('href')) for link in links if link.get('href')]
        sub_urls = [sub_url for sub_url in sub_urls if url in sub_url]

    return sub_urls[:5]
