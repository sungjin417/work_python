# while문 : 참인 동안 반복 수행, 반복횟수를 알 수 없을 떄 주로 사용
# 입력 받은 정수의 합 구하기
# n = int(input("정수 입력 : "))
# sum = 0
# while n:
#     sum += n    # sum에 n값 누적해서 더함
#     n -= 1      # n-- (파이썬에서는 안됨)
# print(sum)      # 파이썬은 왜 들여쓰기를 했을까? 누가 코딩해도 똑같이 하게 하기위해(가독성) , 쉽게하기위해

while True:
    age = int(input("나이를 입력 : "))
    if 0 <= age < 200: break        # Java와 다른점 : 논리연산자가 안들어가고 한번에 씀
    print("나이 입력 범위를 벗어 났습니다.")