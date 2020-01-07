from typing import List, Tuple, Optional

import requests


class WebScraper:
    def __init__(self, sites: List[str]):
        self.sites = dict([(site, False) for site in sites])

    @staticmethod
    def check_on_page(site, text: str) -> bool:
        r = requests.get(site)
        content = r.content
        on_page = content.find(bytes(text, 'UTF-8')) >= 0

        return on_page

    def check_pages(self, text: str) -> Tuple[bool, Optional[str]]:
        for site, found in self.sites.items():
            if found:
                continue

            if self.check_on_page(site, text):
                self.sites[site] = True
                return True, site

        return False, None

    def check_all_found(self) -> bool:
        all_found = all(self.sites.values())

        return all_found
