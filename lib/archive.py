from bs4 import BeautifulSoup as bs
import json

def dump_links():
    with open("./data/archive.html") as fp:
        soup = bs(fp)

    wrappers = soup.find_all("td", class_="archiveLink")
    links = [wrapper.find("a")["href"] for wrapper in wrappers]
    # extract the title, which is just the text contained in the elements in
    # `links`, to be used as the key in the dictionary
    dirty_titles = [link.text for link in wrappers]

    # create a dictionary with the title as the key and the link as the value
    comics = dict(zip(dirty_titles, links))

    # write the links to a file in json format
    with open("./data/comics.json", "w") as fp:
        json.dump(comics, fp)

    # print the number of links extracted, and the first 5 links
    print(f"Extracted {len(links)} links and dumped to /data/links.json")
