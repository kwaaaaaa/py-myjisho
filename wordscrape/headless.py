import logging
import mechanize
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException


class MechSession(object):
    def __enter__(self):
        self.br = mechanize.Browser()
        self.br.set_handle_robots(False)
        self.br.set_header(
            "User-Agent",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36",
        )
        return self.br

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            logging.info(exc_type, exc_val)
            logging.info(exc_tb)

        try:
            self.br.close()
        except Exception, e:
            logging.error("Exception closing mechanize session:", repr(e))


# class SeleniumSession(object):
#     def __enter__(self):
#         option = webdriver.ChromeOptions()
#         option.add_argument(' - incognito')
#         self.br = webdriver.Chrome(
#             executable_path='/Library/Application Support/Google/chromedriver',
#             chrome_options=option
#         )
#         return self.br
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type:
#             logging.info(exc_type, exc_val)
#             logging.info(exc_tb)
#
#         try:
#             self.br.close()
#         except Exception, e:
#             logging.error("Exception closing selenium session:", repr(e))
#
#     def load_url(self, url):
#         timeout = 20
#
#         self.br.get(url)
#
#         try:
#             WebDriverWait(self.br, timeout)
#         except TimeoutException:
#             logging.error("Timed out waiting for page to load")
#             self.br.quit()
