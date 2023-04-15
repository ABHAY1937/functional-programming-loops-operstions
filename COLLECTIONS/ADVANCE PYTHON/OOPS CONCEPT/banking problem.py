#bank name
#account number
#name
#min_balance

#deposite
#cash

#withdraw
#cash


class Bank_details:
    bank='STATE BANK OF INDIA'
    min_balance=2000
    def acc_creation(self,account_number,name):
        self.account_number=account_number
        self.name=name
        self.total=self.min_balance
class Deposite:
    def deposite(self,cash):
        self.cash=cash
        self.total=self.total+self.cash
        print('Your',Bank_details.bank,'aacount has been credited',self.cash,'total balance is',self.total)


    def withdraw(self,cash1):
        self.cash1=cash1
        if self.cash1>self.total:
            print('insufficient balance')
        else:
            self.total=self.total-self,cash1
            print("Your",Bank_details.bank,'account has been debited',self.cash1,'total_balance is',self.total)

account1=Bank_details()
account1.acc_creation(173410400000060154,'ABHAY')
account1.deposite(10000)
account1.withdraw(2500)




