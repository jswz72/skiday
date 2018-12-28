from bs4 import BeautifulSoup
import re


class Cannon(Scraper):
    def _parse(self):
        """
        """
        if not self.soup:
            print('Must make soup first')
            return
        report = {}
        report['conditions'] = self.soup.find('div', id='conditions').find('p').getText()

        heading = self.soup.find(id='cannon-report', class_='report-section')
        hours_string = heading.find(class_='inside-sub-heading').getText()
        hours = hours_string[re.search('\d', hours_string).start():]
        report['hours'] = hours

        data = [item.getText() for item in heading.find_all(class_='datum')]
        nums = [re.findall('\d+', item) for item in data[1:]]
        report['snow'], report['trails'], report['lifts'] = nums
        return report
