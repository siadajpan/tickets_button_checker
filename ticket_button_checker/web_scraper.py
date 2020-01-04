import requests


class WebScraper:
    def __init__(self, site: str):
        self.site = site

    def check_on_page(self, text: str) -> bool:
        r = requests.get(self.site)
        content = r.content
        on_page = content.find(bytes(text, 'UTF-8')) >= 0

        return on_page
