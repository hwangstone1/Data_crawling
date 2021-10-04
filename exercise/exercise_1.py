from bs4 import BeautifulSoup
import requests

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%86%A1%ED%8C%8C+%ED%97%AC%EB%A6%AC%EC%98%A4%EC%8B%9C%ED%8B%B0"

res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

# with open("quiz.html", "w", encoding="utf8") as f:
#     f.write(soup.prettify())
#
items = soup.find("div", attrs={"class": "detail_area"}).find("ul").find_all("li")

for index , item in enumerate(items):
    data = item.find_all("span", attrs={"class":"dsc"})
    for i in range(len(data)):
        print(data[i].get_text())