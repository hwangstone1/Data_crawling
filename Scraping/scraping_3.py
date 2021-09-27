import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list?titleId=183559&weekday=mon"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# cartoons = soup.find_all("td",attrs={"class":"title"})
# text  = cartoons[0].a.get_text()
# link = cartoons[0].a["href"]
# print(text)
# print("https://comic.naver.com/webtoon/list?titleId=183559&weekday=mon" + link)
#
# for i in cartoons:  ## 제목 링크 긁어오기
#     title = i.a.get_text()
#     link = "https://comic.naver.com/webtoon/list?titleId=183559&weekday=mon" + i.a["href"]
#     print(title, link)

sum = 0
cartoons = soup.find_all("div", attrs={"class":"rating_type"})
for i in cartoons:
    starpoint = i.find("strong").get_text()
    sum += float(starpoint)
    print(starpoint)
print("전체전수: ", sum)
print("평균점수", sum / len(cartoons))


