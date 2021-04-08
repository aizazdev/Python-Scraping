import requests
from bs4 import BeautifulSoup

page =requests.get('http://firstround.com/companies/')
soup = BeautifulSoup(page.content, 'html.parser')
main_container = soup.find('div', {'class': 'panel-group'})
containers = main_container.findAll('div', {'class': 'panel-heading'})
for c in containers:

    title = c.find('b').get_text()
    detail = c.find('span', {'class': 'hide-mobile'}).get_text()
    location = c.find('p', {'class': 'company-location'}).get_text()
    link = c.find('a', {'class': 'status-link'})
    if link:
        link = link['href']

    print("___title - > ", title)
    print("___detail - > ", detail)
    print("___location - > ", location)
    print("___link - > ", link)
    print(sep="\n\n\n")
