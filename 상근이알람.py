# 첫째줄에 두정수 H와 M이 주어진다.(0 <= H <= 23, 0<= M <= 59)
# 입력시간은 24시간 표현 사용
# 불필요한 0은 사용 x

hour, min = map(int, input("시간을 입력 : ").split(":"))
tmp = (hour * 60) + min
if tmp < 45:
    tmp = (24 * 60) + min
tmp -= 45
print(f"{tmp//60} {tmp % 60}")