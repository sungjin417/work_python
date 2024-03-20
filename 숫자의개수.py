a = int(input())
b = int(input())
c = int(input())
ls = str(a*b*c)
for i in range(10): # 인덱스가 0부터 9까지 만들어짐
    print(ls.count(str(i)))