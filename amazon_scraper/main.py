import requests
from bs4 import BeautifulSoup

URL = "https://www.amazon.in/Razer-BlackShark-V2-Headset-RZ04-03240100-R3M1/dp/B08WBJHVYV"


content = requests.get(URL)
soup = BeautifulSoup(content.text, features='html.parser')

review_sec = soup.find(attrs={'id': 'cm-cr-dp-review-list'})

reviews = []

for div in review_sec.find_all('div', class_='reviewText'):
    reviews.append(div.span.text)