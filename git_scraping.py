import requests #do your imports at the top of the file
from bs4 import BeautifulSoup

url = 'https://www.govdeals.com/index.cfm?fa=Main.AdvSearchResultsNew&searchPg=Location&inv_num=&category=00&kWord=&kWordSelect=2&sortBy=ad&agency=9557&state=&country=&locID=40686&timing=bySimple&locationType=state&timeType=&timingWithin=1' # THIS IS THE URL THAT WE'RE GRABBING
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}) # OUR REQUEST LIBRARY JUST FETCHES HTML....HEADERS PASSES OUR USER AGENT THROUGH OUR BROWSER
html = response.content # Response.content

soup = BeautifulSoup(html, features="html.parser")
div = soup.find(id="NO_boxx_row") # This is where it gets tricky.  The page doesn't seem to be a "table" per se, more like a bunch of divs that look like a table.  Tried to adjust accordingly but I'm not 100% on scraping these so I could be wrong.


for row in div.find_all('boxx_row'): #tried to get rows with the chunks organized into rows by the div
    for cell in row.find_all('a'): # Another tricky thing, not sure if this is gonna work without it being an actual table
        for cell in row.find_all('label'):
            for cell in row.find_all('#result_col_2 a'):
                for cell in row.find_all('#bid_price'):
        text = cell.text.strip() # get rid of white space
        list_of_cells.append(text) # add them to the outer list
    print(list_of_cells)
