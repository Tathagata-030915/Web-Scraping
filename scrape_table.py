import requests as rq
from bs4 import BeautifulSoup as bs
import pandas as pd

#url = "https://indiawris.gov.in/wris/#/rainfall"
url = "https://ticker.finology.in/"
r = rq.get(url)
print(r)

soup = bs(r.text, "lxml")
table = soup.find("table", class_ = "table table-sm table-hover screenertable")
#print(table)

headers = table.find_all("th")

titles = []
for i in headers :
    titles.append(i.text)

print(titles)

df = pd.DataFrame(columns = titles)
print(df)

