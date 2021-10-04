# chrome without chrome

from bs4 import BeautifulSoup
from selenium import webdriver
import time, requests

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920x1080")


browser = webdriver.Chrome(options=options)
browser.maximize_window()

# 페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

interval = 2

prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # 스크롤을 가장아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    time.sleep(interval)
    # 현재 문서 높이를 가져와서 저장
    curr_height = browser.execute_script("return document.body.scrollHeight")
    if prev_height == curr_height:
        break

    prev_height = curr_height

print("스크롤 완료")
browser.get_screenshot_as_file("google_movie.png")

soup = BeautifulSoup(browser.page_source, "lxml")

# movies = soup.find_all("div", attrs={"class":["ImZGtf mpg5gc", "Vpfmgd"]})
# print(len(movies))
movies = soup.find_all("div", attrs={"class":"Vpfmgd"})


# with open("movie.html", "w", encoding="utf8") as f:
#     f.write(res.text)
# f.write(soup.prettify())

for movie in movies:
    text = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()

    # 할인전 가격
    o_price = movie.find("span", attrs={"class" : "SUZt4c djCuy"})
    if o_price:
        o_price = o_price.get_text()
    else:
        #print(text, "<할인 되지 않은 영화>")
        continue
    # 할인된 가격
    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()

    # 링크 정보

    link = movie.find("a", attrs={"class":"JC71ub"})["href"]
    # 올바른 링크 = https://play.google.com + link

    print(f"제목: {text}")
    print(f"할인 전 가격: {o_price}")
    print(f"할인 후 가격: {price}")
    print("링크: ", "https://play.google.com" + link)
    print("-"*100)

browser.quit()

