import requests
from bs4 import BeautifulSoup

url = 'https://www.ola.state.md.us/Search/Report?keyword=&agencyId=&dateFrom=&dateTo='
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
html = response.content

soup = BeautifulSoup(html, features="html.parser")
table = soup.find('tbody')

for row in table.find_all('tr'):
    for cell in row.find_all('td'): # finds all the td tags and names all of them cells
        print(cell.text) # prints all of them inside the 
