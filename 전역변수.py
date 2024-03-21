# 파이썬의 변수는 함수 스코프 따름,
# 전역에서 선언된 변수 중 immutable 특성을 가진 경우에는 glibal 키워드 사용해야 함
# 대부분의 경우에서 전역변수를 사용하는 것보다 매개변수로 전달하는 것이 문제(Side Effect)
# 발생 확률을 줄일 수 있음
knife = 10
# 전역변수
def game(player):
    global knife
    knife -= player
    print(f"남아있는 칼은 {knife}자루 입니다.")

# 매개변수
def game2(player, knife):
    knife -= player
    print(f"남아있는 칼은 {knife}자루 입니다.")

player = int(input("경기에 참여하는 선수가 몇명 입니까?"))
# game(player)
game2(player, knife)