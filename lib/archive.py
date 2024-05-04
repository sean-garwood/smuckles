from bs4 import BeautifulSoup as bs
import json

def dump_links():
    with open("./data/archive.html") as fp:
        soup = bs(fp)

    #  get wrapping <td> tags with class 'archiveLink'
    wrappers = soup.find_all("td", class_="archiveLink")
    # extract href attrs from all <a> tags contained in the wrappers
    links = [wrapper.find("a")["href"] for wrapper in wrappers]
    # extract dates from links using regex
    # write the links to a file in json format
    with open("./data/links.json", "w") as fp:
        json.dump(links, fp)

    # print the number of links extracted, and the first 5 links
    print(f"Extracted {len(links)} links and dumped to /data/links.json")
