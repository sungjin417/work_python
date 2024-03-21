# pc 방 알바
'''
person = int(input()) # 사람수 입력
k = list(map(int, input().split()))
pc = [0]*100 # 0값으로 초기화된 100의 리스트 생성
cnt = 0

for e in k:
    if pc[e-1] != 0: cnt += 1
    else: pc[e-1] = 1
print(cnt)
'''
# 저항 : 3가지의 값을 조합해서 저항값 구하기
color = "black", "brown", "red", "orange", "yellow", "green", "blue", "violet"
f_name = color.index(input()) # 입력받은 컬러값의 인덱스를 반환
s_name = color.index(input())
t_name = color.index(input())
print(int(str(f_name)+str(s_name) * (10** t_name)))