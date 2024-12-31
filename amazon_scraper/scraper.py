from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from user_agent import generate_user_agent

def scrape_amazon(amazon_product_url: str, parse=False) -> list[str]:
    if parse:
        amazon_product_url = parse_url(amazon_product_url)

    headers: dict[str, str] = {
        'User-Agent': generate_user_agent(),
        "accept-language": "en-GB,en;q=0.9",
    }

    content: requests.Response = requests.get(amazon_product_url, headers=headers)

    soup: BeautifulSoup = BeautifulSoup(content.text, features='html.parser')

    review_sec = soup.find(attrs={'id': 'cm-cr-dp-review-list'})

    product_reviews = []

    for div in review_sec.find_all('div', class_='reviewText'):
        product_reviews.append(div.span.text)

    return product_reviews

def parse_url(initial_url: str) -> str:
    parsed = urlparse(initial_url)

    return parsed.scheme + "://" + parsed.netloc + parsed.path