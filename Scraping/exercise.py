import re
import requests
from bs4 import BeautifulSoup

headers = {"Uses-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"}
menu = ["", "/media/video", "/popular/read"]
for i in menu:
    #bbc-14gzkm2 e19k1v2h0
    #bbc-1sk5sm2 e19k1v2h0
        url = "https://www.bbc.com/korean{}".format(i)
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, "lxml")

        news = soup.find_all("li", attrs={"class":re.compile("^e57qer20")})

        for i in news:
            text = i.find("div", attrs={"class":re.compile("^e19k1v2h0")}) # 기사 제목
            if text:
                text = text.get_text()
            else:
                continue
            print(text)
            # number  = i.find("div", attrs={"class": "bbc-cco6mt erh4ywh3"}).get_text() #기사번호
            # link = i.find("a", attrs={"class":"bbc-bta7jm emesykt4"})["href"]
            # date = i.find("time", attrs={"class":"bbc-1cagdt4 e4zesg50"})
            # if date:
            #     date = date.get_text()
            # else:
            #     date = ""
            # print(number , text, date)
            # print("{}".format("https://www.bbc.com" + link))

