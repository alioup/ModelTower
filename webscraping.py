from lxml import html
from bs4 import BeautifulSoup
from urllib2 import urlopen
import requests

BASE_URL = 'http://whyisthetowerorange.com/'
html = urlopen(BASE_URL).read()
soup = BeautifulSoup(html, "lxml")
reason = soup.select('div[id^=reason]')
if "It's not" in str(reason[0]):
    print "It's not."
else:
    print "The Tower is Orange"

