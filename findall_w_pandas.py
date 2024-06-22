import pandas as pd
import requests as rq
from bs4 import BeautifulSoup as bs

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = rq.get(url)

soup = bs(r.text, "lxml")

names = soup.find_all("a", class_ = "title")
#print(names)

prod_name = []

for i in names :    #we will be iterating these values inside the names list
    name = i.text #each name inside these name will be equal to the value of i.text and then this will be appended to the empty list prod_name
    prod_name.append(name)

print(prod_name)
print(len(prod_name))
print()

prices = soup.find_all("h4", class_ = "price float-end card-title pull-right")

price_list = []

for j in prices :
    price_list.append(j.text)

print(price_list)
print(len(price_list))
print()

desc = soup.find_all("p", class_ = "description")

desc_list = []

for k in desc :
    desc_list.append(k.text)

print(desc_list)
print(len(desc_list))
print()


reviews = soup.find_all("p", class_ = "review-count float-end")
rev_list = []

for a in reviews :
    rev_list.append(a.text)

print(rev_list)
print(len(rev_list))
print()

df = pd.DataFrame({"Product Name" : prod_name, "Prices" : price_list, "Description" : desc_list, "No of reviews" : rev_list})
print(df)

df.to_csv("product_details.csv")
