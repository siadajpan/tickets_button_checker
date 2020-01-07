import time

import settings
from ticket_button_checker.sms_sender import SMSSender
from ticket_button_checker.web_scraper import WebScraper

if __name__ == '__main__':
    ws = WebScraper(settings.SITES)
    sms_sender = SMSSender()

    while True:
        on_page, site = ws.check_pages(settings.TEXT_SEARCHED)

        if on_page:
            sms_sender.send_sms(site)

        if ws.check_all_found():
            break

        time.sleep(10)
