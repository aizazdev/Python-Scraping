from lxml import html
import requests

page = requests.get('http://firstround.com/companies/')
contents = html.fromstring(page.content)
print(contents)