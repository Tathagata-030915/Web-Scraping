import requests as rq
from bs4 import BeautifulSoup as bs

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = rq.get(url)

soup = bs(r.text, "lxml")

prices = soup.find_all("h4", class_ = "price float-end card-title pull-right")
#print(prices)
#print(len(prices))

#for i in prices :
    #print(i.text)
#print(prices[3])

desc = soup.find_all("p", class_ = "description")
print(desc[3])

