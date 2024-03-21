#계좌 개설
def open_account(name): # 매개변수와 반환값이 있는 함수 선언
    print(f"{name}님의 계좌가 개설 되었습니다.")
    return name
def deposit(balance, input): # 잔액과 입금액을 매개변수로 전달 받음(입금)
    print(f"{input}이 입금 되었습니다. 잔액은 {balance+input}입니다.")
    return balance + input
def withdraw(balance, input):
    if balance >= input:
        print(f"{input}이 출금 되었습니다. 잔액은 {balance-input}입니다.")
        return balance - input
    else:
        print("출금이 실패했습니다.")
balance = 0 # 현재 잔액을 외부에서 선언 함 (함수안에서 사용할려면 global을 붙여 global balance를 함수 내부에 넣어야함)
name = open_account("곰돌이사육사")
balance = deposit(balance, 1000)
balance = withdraw(balance, 500)
print(f"{name}의 잔액은 {balance}입니다.")