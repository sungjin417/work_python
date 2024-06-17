import requests
from bs4 import BeautifulSoup
# res = requests.get("https://naver.com")
# print("응답코드 : ", res.status_code)
#
# # if res.status_code == 200:
# #     print("정상 응답 입니다.")
# # else :
# #     print("네트워크 오류 : [에러코드 ", res.status_code, "]" )
#
# # print(res.text)
# soup = BeautifulSoup(res.text, 'lxml')
# # print(soup)
# print(soup.find(attrs={"class":"notify_area"}))

# HTML 문서
html_doc = '''
<html>
  <head>
    <title>Example Page</title>
  </head>
  <body id = "container">
    <h1>Hello, Beautiful Soup!</h1>
    <div class="content">
      <p>This is a paragraph.</p>
      <p>This is another paragraph.</p>
    </div>
    <div class="example">
      <p>This is example.</p>
      <p>This is another example.</p>
    </div>
    <div id = "parent">
        <div class="child">첫 번째 자식</div>
        <div class="child">두 번째 자식</div>
    </div>
    <a href="https://www.example.com">Link</a>
  </body>
</html>
'''
# HTML 문서를 파싱하여 BeautifulSoup 객체 생성
soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup)

# 요소검색
# 타이틀 태그를 검색
title_tag = soup.title
# print(title_tag)
# 클래스가 "content" 인 div 태그를 검색(CSS 선택자를 이용하여 태그를 추출)
div_tags = soup.select("div.content")
# print(div_tags)
for div in div_tags:
    print(div)

# href 속성이 있는 모든 a 태그를 선택
a_tag = soup.find_all("a", href=True)
for a in a_tag:
    print(a)

# Tag 객체 다루기 : Tag 객체에서는 요소의 이름, 속성, 내용 등을 다룸
tag_name = title_tag.name
print(tag_name)
# Tag 객체에서 요소의 속성 얻기
tag_attrs = div_tags[0].attrs
print(tag_attrs)
# Tag 객체에서 요소의 내용 얻기
tag_content = div_tags[0].text
print(tag_content)

# CSS 선택자로 요소 검색하기
div_tags = soup.select("div.example")
print(div_tags)

# id 선택자 사용하기
id_sel = soup.select_one("#container")
print(id_sel)

# 자식 태그 선택자 사용하기
children = soup.select("#parent > .child")
print(children)

# 속성으로 요소 검색하기
attrs = {"class" : "example"}
el = soup.find_all(attrs=attrs)
print(el)