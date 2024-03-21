# 튜플 : 값을 변경 할 수 없는 (immutable) 시퀀스 자료형
# () 소괄호를 사용해서 만들거나 괄호가 없으면 튜플
x = 10
y= 20, # 튜플(y, = 20)
print(type(x))
print(type(y))

person = 'Alice', 30, '곰돌이사육사', True # Packing(나뉘어진 여러가지 데이터를 하나로 묶는것)
print(person)
a,b,c,d = person # Unpacking

# 튜플을 이용한 함수 반환 값 다루기
def get_person():
    name = "곰돌이사육사"
    age = 25
    addr = "경기도 수원시"
    return name, age, addr

name_card = get_person()
print(name_card)
