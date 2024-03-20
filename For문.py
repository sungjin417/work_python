# for문은 정해진 범위 만큼 반복 할 때 주로 사용
# for 요소 in 시퀀스 : 시퀀스는 리스트(수정가능), 튜플(읽기만 가능), 문자열 등을 의미
# 자바의 향상된 for문과 유사
'''
fruits = ["사과", "바나나", "딸기", "수박", "참외", "복숭아"]
for e in fruits:
   # print(e) # 줄바꿈해서 출력
    print(e, end=" ") # 사이에 공백 넣어서 한줄로 출력
print()
# for 변수 in range(시작값, 종료값, 증감값) : 자바의 일반적인 for문과 유사
n = int(input("정수 입력 : "))
sum = 0
for i in range(1, n+1): # 1부터 n까지 순회(마지막(종료값)은 미만개념), 증감값은 생략하면 1씩 증가
    sum += i
print(sum)
'''
'''
# 이중 for문 사용하기
n= int(input("정수를 입력 : "))
for i in range(0, n): # range() 범위를 순회 // 행의 갯수를 의미
    for j in range(0, n): # 열의 갯수를 의미
        print("*", end=" ") # 열이 다 돌아야 행으로 돈다(톱니바퀴처럼)
    print()
'''
'''
#구구단 출력
for i in range(2, 10): # 2 ~ 9까지
    for j in range(1, 10):
        print(f"{i} x {j} = {i*j}")
    print("------------")
'''
# 이중 for문과 조건문 사용
n = int(input("정수를 입력 하세요 : "))
for i in range(0, n):
    for j in range(0, n):
        if j % 2 == 0:
            print("#", end=" ")
        else:
            print("*", end=" ")
    print()