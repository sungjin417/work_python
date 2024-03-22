# score_file = open("./score.txt",  "w", encoding="utf-8")
# print("수학 : 55", file=score_file) # print 값이 score_file에 써짐
# print("영어 : 60", file=score_file) # print()에는 기본적으로 줄바꿈문자가 포함
# score_file.write("과학 : 90\n")
# score_file.write("국어 : 100\n")
# score_file.close()

#파일 읽기
score_file = open("score.txt", "r", encoding="utf-8")
# read() 함수 : 파일내의 모든 내용을 읽어 하나의 문자열로 반환
# print(score_file.read())
# score_file.close()

# readline() 함수 :한 라인씩 읽어 문자열로 반환, 파일의 끝에 도달하면 None값이 반환 됨
# while True:
#     line = score_file.readline()
#     if not line: break
#     print(line, end="")
# score_file.close()

# readlines() : 해당 파일의 모든 라인을 순서대로 읽어 들여 리스트로 반환
# lines = score_file.readlines() # 파일의 라인을 리스트로 반환
# for line in lines:
#     print(line, end="")
# score_file.close()

#with 구문을 사용하면 구문이 종료 될 때, 자동으로 파일을 닫음
with open("scre.txt", "r", encoding="utf-8") as score_file:
    lines = score_file.readlines()
    for line in lines:
        print(line, end="") # close를 안해줌(with를 사용했기 때문)