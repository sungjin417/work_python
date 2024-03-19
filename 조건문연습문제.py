# 3자리의 정수를 입력 받아 100의자리, 10의자리, 1의 자리로 나누어 담고
# 가장 큰 수를 찾아서 출력
# 입력 : 573, 출력 : 7
'''
num = int(input("3자리 정수를 입력 : "))
a = num//100
b = num%100//10
c = num%10
print(max(a,b,c))
'''
# 주/야간 아르바이트 급여 계산
type = int(input("주간근무 [1], 야간근무 [2] : "))
time = float(input("근무 시간을 입력해 주세요 : "))
if type == 1:
    pay = 9620
else:
    pay = 9620 * 1.5

type_str = type == 1 and "주간" or "야간"

money = int(pay * time)
print(f"{time} 시간 동안 근무한 {type_str}급여는 {money}원 입니다.")
