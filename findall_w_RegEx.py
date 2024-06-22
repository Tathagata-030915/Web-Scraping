import requests as rq
from bs4 import BeautifulSoup as bs
import re   #stands for regular expressions; helps us find a pattern in strings and then it extracts the data related to the pattern

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"

r = rq.get(url)

soup = bs(r.text, "lxml")

#data = soup.find_all(["h4", "a", "p"])
#print(data)

#data = soup.find_all(string = "Galaxy Tab")
data = soup.find_all(string = re.compile("Galaxy")) #we will get every name of device with galaxy on using regular expression module "re"
print(len(data))

