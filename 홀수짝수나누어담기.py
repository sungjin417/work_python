# 임의의 수를 연속(공백)으로 입력 받아 홀수, 짝수 리스트로 나누어 담기
# 1 2 3 4 5 6 7 8 9 10
# 홀수 : 1 3 5 7 9
# 짝수 : 2 4 6 8 10
''' # 1전쨰 방법
num = list(map(int, input().split())) # map(함수(ex. int), 리스트(ex. input))
a_list = []
b_list = []

for i in num: # 리스트의 값을 한개씩 끄집어 내면서 순회(시작부터 끝까지 자동순회)
    if i % 2 == 0:
        a_list.append(i)
    else:
        b_list.append(i)
print(f"짝수 : {a_list}\n홀수 : {b_list}")
'''
# 람다로 풀이
num = list(map(int, input("정수 입력 : ").split()))
even = list(filter(lambda x:x % 2 == 0, num)) # 2개의 매개변수가 들어감 (1. 조건이 들어가는 (익명의)함수, 2.요소)
odd = list(filter(lambda x:x % 2 == 1, num))
print(f"짝수 : {even}")
print(f"홀수 : {odd}")
