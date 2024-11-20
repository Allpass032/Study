# 3번 문제 풀이

class BankAccount:
    # 5번 지시사항 transfer 변경
    def __init__(self, acc_no, balance):
        self.acc_no = acc_no
        self.balance = balance
    
    def deposit(self, money):
        if money > 0:
          self.balance += money
        else:
          raise BankError(f"{money} 입금 불가")
    
    def withdraw(self, money):
        if money < 0:
          raise BankError(f'{money} 출금 불가')
        elif money > self.balance:
          raise BankError(f"잔액 부족")
        else:
          self.balance -= money
          return money
    
    def transfer(self, you, money):
        self.withdraw(money)
        you.deposit(money)
        # you.deposit(self.withdraw(money))
    
    def inquiry(self):
      print(f"계좌번호: {self.acc_no}")
      print(f"통장 잔액: {self.balance}")

        
class BankError(Exception):
    def __init__(self, message):
        super().__init__(message)