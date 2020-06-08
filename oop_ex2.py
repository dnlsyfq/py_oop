class BankAccount:

    def set_details(self,name,balance=0):
        self.name = name 
        self.balance = balance

    def display(self):
        print(self.name, self.balance)

    def withdraw(self,amount):
        self.amount = amount 
        self.balance = self.balance-self.amount 
        print("Withdraw: {}, Balance: {}".format(self.amount,self.balance))


    def deposit(self,deposit):
        self.deposit = deposit 
        self.balance = self.balance + self.deposit 
        print("Deposit: {}, Balance: {}".format(self.deposit,self.balance))


matt = BankAccount()
matt.set_details('Maybank',1000)

matt.withdraw(50)

matt.deposit(100)


