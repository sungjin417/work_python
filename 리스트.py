# 리스트란? 연속적으로 저장되는 형태의 자료형, 크기가 동적으로 변함
# 자바와 다른점은 여러가지 데이터 타입이 섞여 있을 수 있음,
# 리스트 안에 리스트가 존재할 수 있음
# 리스트는 읽고 쓰기가 가능, 튜플은 동일한 구조이지만 "읽기"만! 가능
'''
number = [1,2,3,4,5,6,7]
fruits = ['apple', 'banana', 'orange']
mixed = [1, 'apple', True, 3.14,['EV6', 'Santafe', 'Sorento']]

print(number[1])
print(fruits[0])
print(fruits[1][2])
print(mixed[4][2])
print(mixed[4][2][5])
print(mixed[3])
# print(mixed[3][1]) # 3.14는 하나의 덩어리/ '' -> 문자로 이루어진 배열
print(len(mixed[4]))
#print(len(mixed[0])) # 1은 배열이 아니기 때문에 에러가 남
#print(mixed[4][2][10]) # Sorento의 배열을 넘어가기 때문에 에러
print(mixed[4][2][-7])

list_a = [1,2,3]
list_b = [4,5,6]
list_c = list_a + list_b # 리스트를 더하는 것 가능
print(list_c)

new_list = [1,2,3]
new_list.append(4) # append() : 값을 추가
new_list.append(5) # 뒤에 값을 추가 (Java의 add와 같음)
new_list.insert(1, 1000) # 1번 인덱스에 값 추가
'''
'''
# 리스트에서 값 제거하기 : pop, remove, clear, del
# pop : 인덱스가 없으면 마지막 인덱스의 값을 반환하고 삭제
print(new_list.pop()) # 맨 마지막의 5를 반환하고 제거
print(new_list.pop(1)) # 해당 인덱스의 값을 반환하고 제거
new_list.remove(3) # 해당 값을 제거, 동일한 값이 여러개 존재하는 경우, 낮은 인덱스(앞에 것)의 값 제거
print(new_list)
new_list.clear() # 내용을 전부 제거하지만, 리스트는 제거하지 않음
del new_list[3] # 해당 인덱스의 값 제거
print(new_list)
'''
'''
# 변수와 리스트의 차이비교

# 변수
kor, eng, mat = map(int, input().split())
total = kor + eng + mat
print(total/3)
# 리스트
score = list(map(int, input().split()))
print(sum(score)/len(score))
'''
'''
# 중복 제거
my_list = ["A", "B", "C", "D", "B", "C", "E"]
new_list = []
for e in my_list:
    if e not in new_list:
        new_list.append(e)
print(new_list)
'''
'''
# 리스트 순회하기
x = ["John", "George", "Paul", "Ringo"]
# for e in x:
#     print(e, end=" ") # 향상된 for문
for i in range(len(x)):
    print(x[i], end=" ") # 정통적인 for문
'''
# 1 ~ 45까지의 로또 번호 6개를 자동 생성하기, 중복제거
import random
ls = [] # 빈 리스트 생성
while True: # 반복 횟수를 알수 없기 때문에 그냥 참(참인 동안 반목 수행), !!!반드시 탈출 조건 필요!!!
    rand = random.randrange(1,46) # 1~46미만(45), 임의의 값 생성
    if rand not in ls: # ls는 빈 리스트라서 처음에는 포함되지 않음
        ls.append(rand) # if가 참인 경우 실행
    if len(ls) == 6: break #
print(ls)














