# from simple_colors import *
#
# print(green('hello'))
# print(green('hello', 'bold'))
# print(green('hello', ['bold', 'underlined']))
#
# print(blue('hello'))
# print(blue('hello', 'bold'))
# print(blue('hello', ['bold', 'underlined']))

import requests
from bs4 import BeautifulSoup
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
# HTTP GET 요청
response = requests.get(url)
# HTML 파싱
soup = BeautifulSoup(response.text, "html.parser")
print(soup)
for loc in soup.select("location"):
    print("도시 : ", loc.select_one("city").string)
    print("날씨 : ", loc.select_one("wf").string)
    print("최저기온 : ", loc.select_one("tmn").string)
    print("최고기온 : ", loc.select_one("tmx").string)
    print("-"*20)