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
    titles.append(i.text.strip())

print(titles)

df = pd.DataFrame(columns = titles)
#print(df)

rows = table.find_all("tr")

for i in rows[1:] :     #skipping the part which is on index 0 as we have already obtained it in our th tag
    #print(i.text)
    data = i.find_all("td")
    #print(data)
    row = [tr.text.strip() for tr in data]
    #print(row)
    l = len(df)
    df.loc[l] = row

print(df)
df.to_csv("stock_market_data.csv")






