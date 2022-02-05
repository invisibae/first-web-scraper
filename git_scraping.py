import requests #do your imports at the top of the file

url = 'https://www.govdeals.com/index.cfm?fa=Main.AdvSearchResultsNew&searchPg=Location&inv_num=&category=00&kWord=&kWordSelect=2&sortBy=ad&agency=9557&state=&country=&locID=40686&timing=bySimple&locationType=state&timeType=&timingWithin=1' # THIS IS THE URL THAT WE'RE GRABBING
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}) # OUR REQUEST LIBRARY JUST FETCHES HTML....HEADERS PASSES OUR USER AGENT THROUGH OUR BROWSER
html = response.content # Response.content
print(html)
