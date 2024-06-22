import requests as rq

def fetch_save_file(url, path):
    r = rq.get(url)
    with open(path, "w", encoding = "utf-8") as f:
        f.write(r.text)

url = "https://timesofindia.indiatimes.com/city/delhi"

fetch_save_file(url, "data/times.html")
