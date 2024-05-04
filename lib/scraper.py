from bs4 import BeautifulSoup as bs
import json
import regex as re

def extract_rel(link):
    with open(link, verify=False) as fp:
        soup = bs(fp)

    date = re.search(r"\d{4}/\d{2}/\d{2}", link).group()
    comic = soup.find("img", class_="comicImage")
    return comic, date

def dump_to_html(comic, date):
    output_filename = f"./comics/{date.text}.html"
    with open(output_filename, "w") as fp:
        fp.write("<!DOCTYPE html>\n", comic.prettify(), date.prettify())
        fp.close()

def scraper():
    with open("./data/links.json") as fp:
        archive = json.load(fp)

    for link in archive:
        comic, date = extract_rel(link)
        dump_to_html(comic, date)
        print(f"Extracted comic to comics/`{date.text}`.")

    print(f"Extracted {len(archive)} comics.")
