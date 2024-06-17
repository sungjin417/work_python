from bs4 import BeautifulSoup
#
# # 웹피이지 크롤링
# html = '''
# <html>
#     <table border=1>
#         <tr>
#             <td> 항목 </td>
#             <td> 2013 </td>
#             <td> 2014 </td>
#             <td> 2015 </td>
#         </tr>
#         <tr>
#             <td> 매출액 </td>
#             <td> 100 </td>
#             <td> 200 </td>
#             <td> 300 </td>
#         </tr>
#     </table>
# </html>
# '''
# soup = BeautifulSoup(html, 'html.parser')
# result = soup.select('td')
# # print(result)
# # 정보만 추출할 때
# for e in result :
#     print(e.text)

html = """
<ul>
    <li> 100 </li> 
    <li> 200 </li>
</ul> 
<ol>
    <li> 300 </li> 
    <li> 400 </li>
</ol>
"""
soup = BeautifulSoup(html, 'html5lib')
result = soup.select('ul li') # ul 밑에 li 태그 = ('ul > li')
for e in result :
    print(e.text)