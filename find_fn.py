import requests as rq
from bs4 import BeautifulSoup as bs

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = rq.get(url)

soup = bs(r.text, "lxml")
#print(soup.find('div'))
price = (soup.find("h4", {"class" : "price float-end card-title pull-right"})) #sometimes same tags may have different classes; therefore to get the specific class mention the class name in the form of a python dictionary

print(price.string)

desc = (soup.find("p", {"class" : "description card-text"}))
print(desc.string)
print(soup.find("p", class_ = "description").string)

#find() dunction is limited to the first tag it gets that is specified in the python script


