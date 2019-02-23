from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

Url = 'https://www.eeoc.gov/eeoc/newsroom/release/index.cfm'

regex = re.compile('/eeoc/newsroom/release/.*cfm')

html = urlopen(Url)
bsObj = BeautifulSoup(html.read(), 'lxml')
tag = bsObj.find('div', {'id':'cs_control_4152'})
test = str(tag.find('a'))
search = re.search(regex, test)
print(search.group())
