# 이름 입력
# 나이 입력 : 1 ~ 199까지 입력 받고 잘못된 값이 오면 재 입력 요청을 한다.
# 성별 입력 : 영문자 (M과m은 남성) (F와 f는 여성)으로
#            입력 받고 나머지는 재 입력 요청을 한다.
# 직업 입력 : 1(학생), 2(회사원), 3(주부), 4(무직)으로 입력 받고
#            나머지는 재 입력 요청 한다.
# 결과는 마지막에 한번에 출력 한다.
name = input("이름 입력 : ")
while True:
    age = int(input("나이 입력 : "))
    if 1<=age<=199: break
    print("재 입력 해주세요")
while True:
    gender = input("성별 입력 : ")
    if gender == "M"or"n":
        gender = "남성"
        break
    elif gender == "F"or"f":
        gender = "여성"
        break
    else:
        print("재 입력 해주세요")
while True:
    job = int(input("1(학생),2(회사원),3(주부),4(무직) : "))
    print(f"{job}")
    if 0 < job < 5: break
    print("재입력 해주세요")