from bs4 import BeautifulSoup
import re, requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"}
url = "https://www.op.gg/champion/statistics"
res = requests.get(url, headers= headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find("div", attrs={"class" : "champion-index__champion-list"}).find_all("div", attrs={"class":"champion-index__champion-item__name"})
for index, i in enumerate(items):
    prin = i.get_text()
    print("{}번째 챔피언 : {}".format(index, prin))
