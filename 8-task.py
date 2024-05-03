import requests
import bs4
import lxml

request=requests.get("https://tribuna.uz/")
soup=bs4.BeautifulSoup(request.content, "lxml")

result=soup.select(".news-title")
print(result)
