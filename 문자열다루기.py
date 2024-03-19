# 문자열이란 ? 문자로 이루어진 데이터의 집합, 파이썬은 문자를 별도로 다루지 않고 전부 문자열로 간주
# "", '' (1줄 짜리 문자열), """ """, ''' '''(여러줄의 문자열/주석처리도 가능)
# 인덱싱이란? 시퀀스 자료형(리스트, 튜플, 문자열)에서 특정 위치의 요소(문자)를 선택 하는 작업, seq[index]
# 슬라이싱이란 : 시퀀스 자료형(각각의 요소들이 연속적으로 이어진 자료형)에서 일부분을 추출, seq[start:end:step]
my_list = [0,1,2,3,4,5,6,7,8,9] # 리스트 생성[]
slice_without_step = my_list[2:7] # 인덱스는 0부터 시작, end는 7미만
slice_without_step = my_list[1:9:2] # 1부터 시작 9미만 2칸씩 띄어서(1,3,5,7)
# 인덱싱, 슬라이싱 실습
# 주민등록번호 자르기, 하위 7자리중 첫번째 글자는 성별, 앞의 6자리는 년,월,일
jumin = "991120-1234567"
print("성별 : " + jumin[7])
print("년 : " + jumin[:2]) # 0부터 2미만
print("월 : " + jumin[2:4]) # 2부터 4미만
print("일 : " + jumin[4:6]) # 4부터 6미만
print("생년월일 : " + jumin[:6])
print("뒤 7자리 : " + jumin[7:]) # 7에서부터 끝까지
print("뒤 7자리 : " + jumin[-7:]) # 뒤에서 7자리 부터 끝까지

python_str = "Life is too short, You need Python"
new_str = python_str[0] + python_str[1] +python_str[2] + python_str[3]
# python_str[0] = "l" # 리터럴 상수(문자가 이미 저장되어 있음)이기 때문에 문자 변경 안됨
print(new_str)

# 대소문자 바꾸기 : upper(), loWer()
print(python_str.upper()) # 대문자로 변환
print(python_str.lower()) # 소문자로 변환
# 문자열 변경
a_str = "Hello Python Program"
print(a_str.replace("Python", "JavaScript")) # 글자는 바뀌었지만, 원판은 바뀌지 않았다.

a_str2 = "Hello Python Program"
new_str2 = a_str2.replace("Python", "JavaScript")
print(new_str2) # 새로운 변수에 담았기 때문에 파이썬이 자바스크립트로 바뀌었다.

# 문자열에 포함된 문자 갯수 세기, 문자열 길이( len(), __len__() )
print(a_str2.count("l")) # 해당 문자열에서 count()함수에 전달된 문자가 몇개 존재하는지 반환
print(len(a_str2)) # 문자열 길이를 반환하는 함수
print(a_str2.__len__()) # 문자열 길이를 반환하는 내장 함수

# 문자열 찾기
# find() : 찾은 문자열 인덱스 반환, 없으면 -1
# index() : 찾은 문자열 인덱스 반환, 없으면 ValueError
# rfind() : 뒤에서 부터 문자열을 찾지만, 찾은 인덱스는 앞에서 부터 계산해서 인덱스 반환
phrase = "가장 큰 실수는 포기, 가장 어리석은 일은 남의 결점 찾기, 가장 좋은 선물은 용서"
print(phrase.find("가장"))
print(phrase.rfind("가장"))
print(phrase.index("포기"))
print(phrase.find("나에게")) # 죽지않고(에러는 안나고) -1반환
#print(phrase.index("나에게")) # 죽는다(에러발생)
new_str = phrase.replace("가장", "나에게")
print(new_str)

# 문자열 연산자 : "문자열" + "문자열", "문자열"*3
print("태양고" + "나희도")
print("태양고" * 2)
#print("태양고" + 2) # "문자열" + 2 는 안됨

#문자열 양옆의 공백 제거 : strip()
input_a = """
    안녕하세요. 
  문자열 함수를 알아 봅니다.
   감사합니다.    
    """
print(input_a.strip()) # 맨앞과 맨뒤의 공백을 제거!!