import requests as rq
from bs4 import BeautifulSoup as bs

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"

r = rq.get(url)

soup = bs(r.text, "lxml")

#boxes = soup.find_all("div", class_ = "product-wrapper card-body")
#print(boxes)
#print(len(boxes))

#box = soup.find_all("div", class_ = #"product-wrapper card-body")[3]
#print(box)

#name = box.find("a").text
#print(name)

#desc = box.find("p", class_ = "description").text
#print(desc)

navbar = soup.find_all("ul", class_ = "nav flex-column", id = "side-menu")[0]

name = soup.find("li", class_ = "nav-item active")
print(name.text)
