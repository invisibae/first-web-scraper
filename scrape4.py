import requests
from bs4 import BeautifulSoup

url = 'https://www.ola.state.md.us/Search/Report?keyword=&agencyId=&dateFrom=&dateTo='
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content

soup = BeautifulSoup(html, features="html.parser")
table = soup.find('tbody')

for row in table.find_all('tr'): #introduces our first loop...finds all tr(table row) objects within our table # those will be named "row"
    print(row.prettify()) # print a pretty version
