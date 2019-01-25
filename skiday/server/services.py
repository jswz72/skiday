import requests
from urllib3.exceptions import HTTPError
import server.scrapers as scrapers
import server.storage as storage

def get_webpage(resort):
    url = storage.get_url(resort)
    print('debug ', url);
    req = requests.get(url)
    if req.status_code // 100 in [4, 5]:
        raise HTTPError(f'Bad status code: {req.status_code}')
        return
    return req.text

def get_resort_data(resort):
    try:
        webpage = get_webpage(resort)
        return scrapers.scrape(resort, webpage)
    except HTTPError as err:
        print(err)
        return

def update_resort_data(resort):
    data = get_resort_data(resort)
    print(data)
    if not data:
        print(f'Resort data not written for {resort}')
    storage.write_resort_data(resort, data)


