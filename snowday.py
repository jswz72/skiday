from bs4 import BeautifulSoup
import requests
import re

#r = requests.get('https://www.cannonmt.com/mountain-report')
#f = open('cannon.txt', 'w')
#f.write(r.text)
#f.close()
f = open('cannon.txt', 'r')
webpage = f.read()
f.close()
soup = BeautifulSoup(webpage, 'html.parser')
report = {}
report['conditions'] = soup.find('div', id='conditions').find('p').getText()

heading = soup.find(id='cannon-report', class_='report-section')
hours_string = heading.find(class_='inside-sub-heading').getText()
hours = hours_string[re.search('\d', hours_string).start():]
report['hours'] = hours

data = [item.getText() for item in heading.find_all(class_='datum')]
nums = [re.findall('\d+', item) for item in data[1:]]
report['snow'], report['trails'], report['lifts'] = nums
print(report)
