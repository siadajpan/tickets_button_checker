import time

import settings
from ticket_button_checker.sms_sender import SMSSender
from ticket_button_checker.web_scraper import WebScraper

if __name__ == '__main__':
    ws = WebScraper(settings.SITE)
    sms_sender = SMSSender()

    while True:
        on_page = ws.check_on_page(settings.TEXT_SEARCHED)

        if on_page:
            print('text found on page')
            sms_sender.send_sms()
            break

        time.sleep(10)
