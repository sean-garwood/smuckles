# Comic class to construct comic objects
# ingest pandas dataframe and return comic objects
class Comic:
    def __init__(self, title, url, img_url):
        self.title = title
        self.url = url
        self.img_url = img_url

    def __str__(self):
        return f"Title: {self.title}\nURL: {self.url}\nImage URL: {self.img_url}"
