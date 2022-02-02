# we need to be able to store cells in containers

import requests
from bs4 import BeautifulSoup

url = 'https://www.ola.state.md.us/Search/Report?keyword=&agencyId=&dateFrom=&dateTo='
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content

soup = BeautifulSoup(html, features="html.parser")
table = soup.find('tbody')

for row in table.find_all('tr'):
    list_of_cells = [] # create an empty list of cells to populate
    for cell in row.find_all('td'): # find the rows in the table
        text = cell.text.strip() # get rid of white space
        list_of_cells.append(text) # add them to the outer list
    print(list_of_cells)
