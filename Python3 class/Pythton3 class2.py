class BankAccount:
    def __init__(self,owner,balance = 0):
        self.owner = owner #账号主人
        self.balance = balance #账号余额

    def deposite(self,amount): #存款
        if amount > 0:
            self.balance += amount
            print(f'{self.owner},存入{amount}元，当前余额{self.balance}元！')
    
    def withdrawal(self,amount): #取款
        if amount  <= self.balance:
            self.balance -= amount
            print(f'{self.owner},取出{amount}元，当前余额{self.balance}元！')
        else:
            print('余额不足！')
    #使用

myaccount = BankAccount("Phil",100)
myaccount.deposite(40)
myaccount.withdrawal(10)