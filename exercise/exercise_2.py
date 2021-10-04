#오늘의 날씨
#헤드라인 뉴스
#IT 뉴스
#오늘의 영어

from bs4 import BeautifulSoup
import requests , re

def create_soup(url):
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36"}
    res = requests.get(url,headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    return soup

def print_news(index, title, link):
    print("{}. {}".format(index + 1, title))
    print("  (link) : {}".format(link))


def scrape_weather():
    print("[ Naver 오늘의 날씨 ]")
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%98%A4%EB%8A%98%EC%9D%98+%EB%82%A0%EC%94%A8"
    soup = create_soup(url)

    cast = soup.find("p",attrs={"class":"summary"}).get_text() # 오늘 날씨
    curr_now, curr_max, curr_min = None, None, None
    curr_now = soup.find("div", attrs={"class":"temperature_text"}).get_text() # 현재 온도
    curr_max = soup.find("span", attrs={"class":"highest"}).get_text() # 최고 기온
    curr_min = soup.find("span", attrs={"class":"lowest"}).get_text() # 최저 기온
    am_rainfall = soup.find("span", attrs={"class":"rainfall"}).get_text()
    pm_rainfall = soup.find("span", attrs={"class":"rainfall"}).get_text()
    day = soup.find("span", attrs={"class":"date"}).get_text().replace('.','')
    dust = soup.find("div", attrs={"class":"report_card_wrap"}).find_all("span", attrs={"class":"txt"})
    dust1 = dust[0].get_text()
    dust2 = dust[1].get_text()


    # 출력
    print(cast)
    print("현재 {} ( 최저{} / 최고{})".format(curr_now, curr_min, curr_max))
    print("{} 오전 {} / 오후 {}".format(day, am_rainfall, pm_rainfall))
    print("미세먼지 : {}".format(dust1))
    print("초미세먼지: {}".format(dust2))
    print("*"*50)


def scrape_headline_news():
    print("[Naver headline news]")
    url = "https://news.naver.com"
    soup = create_soup(url)

    news_list = soup.find("ul", attrs={"class":"hdline_article_list"}).find_all("li", limit=5)
    for index, news in enumerate(news_list):
        title = news.div.a.get_text().strip()
        link = url + news.find("a")["href"]
        print_news(index, title, link)
    print("*"*50)

def scrape_it_news():
    print(" IT news")
    url = "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230"
    soup = create_soup(url)

    it_items = soup.find("ul", attrs={"class":"type06_headline"}).find_all("li", limit=10)
    for index , item in enumerate(it_items):
        a_idx = 0
        img = item.find("img")
        if img:
            a_idx = 1  # img 태그가 있으면 1번째 a 태그의 정보를사용

        title = item.find_all("a")[a_idx].get_text().strip()
        link = item.find("a")["href"]
        print_news(index, title, link)
    print("*"*50)

def scrape_english():
    print("[오늘의 영어 회화]")
    url = "https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_lnb_eng_I_others_english&logger_kw=haceng_submain_lnb_eng_I_others_english"
    soup = create_soup(url)

    language = soup.find_all("div", attrs={"id":re.compile("^conv_kor_t")})
    print("(영어 지문)")
    for i in language[len(language)//2:]: # 8문장이 있다고 가정
        print(i.get_text().strip())
    print("\n")
    print("(한글 지문)")
    for i in language[:len(language)//2]:
        print(i.get_text().strip())




if __name__ == "__main__":
    scrape_weather()   # 오늘의 날씨정보 가져오기
    scrape_headline_news() # 헤드라인 뉴스정보 가져오기
    scrape_it_news()
    scrape_english() # 오늘의 영어회화 가져오기