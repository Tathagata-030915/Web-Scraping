import requests as rq
from bs4 import BeautifulSoup as bs

with open("sample.html", "r") as f :
    html_doc = f.read()

soup = bs(html_doc, 'html.parser')  #soup object
#print(soup.prettify())  #print the soup object in a pretty format
#print(soup.title, type(soup.title))

#print(soup.find_all("div"))  #to get all divs
#print(soup.find_all("div")[0])  #to get 1st div

for link in soup.find_all("a") :
    print(link.get("href"))
    print(link.get_text())

s = soup.find(id = "link3")
print(s)