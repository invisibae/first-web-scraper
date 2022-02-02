import csv # importing the csv library to be able to write csv's # standard library imports first (like csv) and external library imports second
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
        if cell.find('a'):
            list_of_cells.append(cell.find('a')['href'])
        text = cell.text.strip()
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

outfile = open("./reports.csv", "w") # we have to name the destination and open the file for writing
writer = csv.writer(outfile) #csv.writer confirms that the file is a csv.  Automatically escapes internal commas.
writer.writerows(list_of_rows) # writes from a list in which each list contains a row 
