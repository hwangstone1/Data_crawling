import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"}
url = 'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230'

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find("div", attrs={"class":"list_body newsflash_body"}).find_all("li", limit =30)

data = {}

for i in items:
    a_idx = 0

    img = i.find("img")
    if img:
        a_idx = 1
    title = i.find_all("a")[a_idx].get_text().strip()
    link =i.find("a")["href"]

    data[title] = link

print(len(data))

for t, l  in data.items():
    print(t, l)
