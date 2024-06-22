import requests as rq
from bs4 import BeautifulSoup as bs

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"
r = rq.get(url)
#print(r)

soup = bs(r.text, "lxml")
print(soup)


