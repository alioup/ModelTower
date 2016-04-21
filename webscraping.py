from lxml import html
from bs4 import BeautifulSoup
from urllib2 import urlopen
import requests

BASE_URL = 'http://whyisthetowerorange.com/'
html = urlopen(BASE_URL).read()
soup = BeautifulSoup(html, "lxml")
reason = soup.select('div[id^=reason]')
print reason

