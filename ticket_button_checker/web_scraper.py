from typing import List, Tuple, Optional

import requests


class WebScraper:
    def __init__(self, sites: List[str]):
        self.sites = dict([(site, False) for site in sites])

    def check_on_page(self, text: str) -> bool:
        r = requests.get(self.site)
        content = r.content
        on_page = content.find(bytes(text, 'UTF-8')) >= 0

        return on_page
