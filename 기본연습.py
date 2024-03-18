print("Hello,python !!!")
print(100)
print(100+200)
name = "곰돌이사육사" # 파이썬은 데이터 타입이 없음, 반드시
print(name)

 # 파이썬의 주석은 #입니다.
name = "정경수"
email = "jks2024@gmail.com"
position = "강사"
addr = "서울시 강남구 역삼동 kh 정보 교육원"
print(f"""
주소 : {addr}
직책 : {position}
이름 : {name}
이메일 : {email}
""")

if True:
    print("정상")
# print("rkekdkk") 줄 안맞으면 에러남
else:
    print("에러")

''' 큰따옴표,작은따옴표 3개 를 넣어도 주석 처리 됨
작성자 : 정경수
목적 : 파이썬 연습용 프로그램
날짜 : 20204.03.18
'''
print(38) # 숫자를 출력
print("문자열 출력")
print([1,2,3]) # list 출력