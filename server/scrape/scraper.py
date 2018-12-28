import requests
import bs4 from BeautifulSoup

class Scraper:
    def __init__(self):
        self.url = None
        self.soup = None

    def run(self):
        self._get_page()
        return self._parse()

    def _get_page(self):
        """ Populate self.soup with requested url html """
        if not self.url:
            print('Error: Must provide url')
            return
        req = requests.get(url)
        if req.status_code // 100 in [4, 5]:
            print('Error: bad status code')
            print(req.status_code)
            return
        self.webpage = BeautifulSoup(req.text, 'html.parser')

    def _parse(self):
        """
        Parse self.soup
        Returns: dictionary containing parsed fields
        """
        return {}
