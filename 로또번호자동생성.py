import random
print("번호 자동 생성 : ", end="")

ls = []
while True:
    rand = random.randrange(1,46)
    if rand not in ls: # 리스트내에서 존재 여부 확인
        ls.append(rand)
    if len(ls) == 6: break
print(ls)