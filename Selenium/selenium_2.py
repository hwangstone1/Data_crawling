from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()

url = "https://beta-flight.naver.com/"
browser.get(url) # url 로 이동

browser.find_element_by_link_text("가는날").click()

# 이전달 선택
# browser.find_elements_by_link_text("27")[0].click()
# browser.find_elements_by_link_text("28")[0].click()

# 다음달 선택
# browser.find_elements_by_link_text("27")[1].click()
# browser.find_elements_by_link_text("28")[1].click()

# 이번달 27일 다음달 28일 선택
#browser.find_elements_by_link_text("27")[0].click()
#browser.find_elements_by_link_text("28")[1].click()

# 위치선택
browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[9]/div/ul/li[1]").click()
browser.find_elements_by_link_text("항공권 검색").click()

