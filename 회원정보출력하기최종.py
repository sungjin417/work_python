
def input_age():
    while True:
        age = input("나이를 입력 : ")
        if age.isdigit(): # 문자열이 숫자로 구성되어 있는지 확인
            age = int(age)
            if 0 < age < 200:
                return age
        print("나이를 잘 못 입력 했습니다.")

def input_gender():
    while True:
        gender = input("성별 입력 : ")
        if gender == "M" or gender == "m": return "남성"
        elif gender == "F" or gender == "f": return "여성"
        print("성별을 잘 못 입력했습니다.")

def input_jobs():
    while True:
        jobs = input("직업을 입력 : ")
        if jobs.isdigit():
            jobs = int(jobs)
            if 0 < jobs < 5: return jobs
        print("직업을 잘 못 입력 하셨습니다.")
# []리스트, {}딕셔너리, ()튜플
def print_info(name,age,gender,jobs):
    jobs_str = "", "학생", "회사원", "주부", "무직" # 튜플(읽는 용도로만 사용)
    print("="*3, "회원정보", "="*3)
    return f"이름 : {name}\n나이 : {age}\n성별 : {gender}\n직업 : {jobs_str[jobs]}"

# 함수호출과 파일저장하기
fd = open("member.txt", "wt", encoding="utf-8") # encoding="utf-8" : 한글부분 안깨짐
while True:
    name = input("이름 입력 / 종료는 quit : ")
    if name == "quit": break
    age = input_age()
    gender = input_gender()
    jobs = input_jobs()
    rst = print_info(name, age, gender, jobs)
    fd.write(rst + "\n")
fd.close()