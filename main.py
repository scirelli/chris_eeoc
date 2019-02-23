#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests

PROTOCAL = 'https://'
DOMAIN = 'www.eeoc.gov'
URL = f"{PROTOCAL}{DOMAIN}/eeoc/newsroom/release/index.cfm"

html = requests.get(URL)
bsObj = BeautifulSoup(html.text)
allAnchors = bsObj.select('#cs_control_4152 a[href]')
for a in allAnchors:
    print(f"{PROTOCAL}{DOMAIN}{a['href']}")
