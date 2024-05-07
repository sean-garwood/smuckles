import json
import regex as re
import requests as rq

def get_links():
    with open('./data/links.json', 'r') as f:
        return json.load(f)

def get_date(url):
    return re.search(r'\d{4}/\d{2}/\d{2}', url).group()

def get_comic(date):
    date = re.sub(r'(\d{4})/(\d{2})/(\d{2})', r'\2\3\1', date)
    url = f"https://achewood.com/assets/img/{date}.png"
    try:
        response = rq.get(url, timeout=1.5)
        file_date = re.sub(r'(\d{2})(\d{2})(\d{4})', r'\3\1\2', date)
        with open(f'./comics/{file_date}.png', 'wb') as f:
            f.write(response.content)
        print(f"Scraped {date}")

    except rq.exceptions.ConnectionError:
        print("Failed to establish a connection. Please check your network.")

def scrape_comics():
    links = get_links()
    for link in links:
        date = get_date(link)
        get_comic(date)
