from lxml import html
import requests

page = requests.get('http://whyisthetowerorange.com/')
tree = html.fromstring(page.content)
reason = tree.xpath('//div[@id="reason"]/text()')
print reason

