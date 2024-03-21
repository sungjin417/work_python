# 딕셔너리 : {}, 키와 값의 쌍으로 이루어져 있음, 자바의 HashMap과 동일구조
# 키와 값은 콜론으로 구분
dict = {"정경수":90, "고유림":88, "나희도":89}
print(dict.keys())
print(dict.values())
print(dict.items()) # key와 values의 값이 담김
print("고유림" in dict) # dict에 포함여부 확인
print("안유진" in dict) # 참이면 T, 거짓이면 F

if "고유림" in dict: # dict안에 "고유림"이 있으면,
    print(dict["고유림"]) # 키값을 가지고 값을 뽑아냄