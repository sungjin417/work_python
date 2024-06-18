import schedule # 스케쥴 기능을 사용하기 위해 import
import time # 일정 시간 만큼 대기를 걸기 위해서
import requests # 서버와 http 동기 통신을 하기 위해서 사용
from bs4 import BeautifulSoup # html 파싱해서 원하는 정보를 추출하기 위해 사용

def perform_web_crawling():
    url = "http://www.naver.com"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
    print(soup)

def job():
    print ("웹 크롤링을 수행 합니다")
    perform_web_crawling()

# schedule.every().day.at("09:45").do(job)
schedule.every(1).minutes.do(job)

while True:
    schedule.run_pending() # 대기 중인 작업을 수행하는 함수
    time.sleep(1) # 1초 대기
#     print(len(response.text))
#
# perform_web_crawling()
