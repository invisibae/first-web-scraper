import requests
from bs4 import BeautifulSoup

url = 'https://www.ola.state.md.us/Search/Report?keyword=&agencyId=&dateFrom=&dateTo='
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content

soup = BeautifulSoup(html, features="html.parser")
table = soup.find('tbody')

list_of_rows = []
for row in table.find_all('tr'):
    list_of_cells = []
    for cell in row.find_all('td'):
        if cell.find('a'): # we need to interrupt the process of looping through the td tags to check for links
            list_of_cells.append(cell.find('a')['href']) # "If this cell contains an 'a' tag we want the FIRST link AND TO APPEND THAT TO THE LIST OF CELLS " # we're grabbing the href because it is the link
        text = cell.text.strip()
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

print(list_of_rows)

# This produces a list that includes relative URL's for each listed item
