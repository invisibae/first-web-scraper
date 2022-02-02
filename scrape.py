import requests #do your imports at the top of the file

url = 'https://www.ola.state.md.us/Search/Report?keyword=&agencyId=&dateFrom=&dateTo=' # THIS IS THE URL THAT WE'RE GRABBING
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}) # OUR REQUEST LIBRARY JUST FETCHES HTML....HEADERS PASSES OUR USER AGENT THROUGH OUR BROWSER
html = response.content # Response.content
print(html)
