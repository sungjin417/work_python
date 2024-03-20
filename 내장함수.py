# 내장 함수? 별도의 import 없이 사용할 수 있도록 내장된 함수를 말함
print(max(32, 45,48, 57, 23))
print(min(32, 45,48, 57, 23))
# sum에는 리스트 혹은 튜플 형태로 전달
print(sum([26, 34, 45, 67, 67])) # 리스트
print(sum((26, 34, 45, 67, 67))) # 튜플 (반환값을 여러개 가질 수 있다)
value = 1,2,3,4,5,6,7,8,9,10 # 튜플
print(sum(value))
print(f"평균 : {sum(value)/len(value)}")
# 몫과 나머지 (divmod) # 튜플을 사용했기 때문에
print(divmod(sum(value), 4))

# 외장함수 : 파이썬의 표준 모듈(파일을 땡겨 온다)이지만, import해야 사용 가능
# 참고 : 내장함수 import시 파일이름과 import이름이 같은 경우
# AttributeError: partially initialized module 'random' has no attribute 'randrange’ 에러가 발생 합니다.
# 이런 경우 import 이름과 파일이름을 다르게 변경하시면 됩니다.
import random

for i in range(10):
    #rand = random.randint(0, 4)  # 0~4사이의 임의의 정수 반환 (4가 포함)
    #rand = random.randrange(0, 4) # 0~4 미만 (4 포함x)
    rand = random.randrange(4)  # 0~4 미만 (4 포함x)
    print(rand)

# 날짜 및 시간 관련처리 모듈
'''import datetime 
datetime.datetime.today()''' # 아래와 같은 코딩
from datetime import datetime # datetime 모듈에서 datetime 함수만 import
datetime.today() # 현재 날짜 가져오기
print(datetime.today().year) # 현재 연도 가져오기
print(datetime.today().month)
print(datetime.today().day)
print(datetime.today().hour)
print(datetime.today().minute)
print(datetime.today().second)
print(datetime.today().microsecond)

# 달력 생성
import calendar
print(calendar.calendar(20204))
print(calendar.calendar(20204, m=5))
print(calendar.month(2024, 3))

# math 모듈
import math
print(math.sin(100))
print(math.cos(100))
print(math.tan(100))
print(math.ceil(1.000001))
print(math.floor(1.000001))

