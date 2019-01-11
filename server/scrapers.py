from bs4 import BeautifulSoup
import re

def scrape_cannon(soup):
    report = {}
    report['conditions'] = soup.find('div', id='conditions').find('p').getText()

    heading = soup.find(id='cannon-report', class_='report-section')
    hours_string = heading.find(class_='inside-sub-heading').getText()
    hours = hours_string[re.search('\d', hours_string).start():]
    report['hours'] = hours

    data = [item.getText() for item in heading.find_all(class_='datum')]
    nums = [re.findall('\d+', item) for item in data[1:]]
    report['snow'], report['trails'], report['lifts'] = nums
    return report

scrapers = {
    'cannon': scrape_cannon,
}

def scrape(title, webpage):
    soup = BeautifulSoup(webpage, 'html.parser')
    if title not in scrapers:
        print(f'No scraper found for {title}')
        return
    return scrapers[title](soup)

