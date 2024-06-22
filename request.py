import requests as rq

url = "https://courses.wscubetech.com"

r = rq.get(url)
#print(r.status_code)    #output = 401 --> unauthorized; we cannot obtain the html of the website
print(r.text)  #output = HTML content of the webpage
