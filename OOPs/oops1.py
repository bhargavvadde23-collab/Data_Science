'''
OOPs is object oriented programming system is a programming approach that uses classes and 
objects to design and build applications, enables the code resuability,readability..
OOPs allows to model real world scenarios like banking system,railway system tec...

'''










#Banking system using class and objects
'''
class BankAccount():
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    
    def deposit(self,amount):
        self.balance+=amount
        
        print(f"{amount} is deposited , available balance is {self.balance}")
        
    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficient balance")
        else:
            self.balance-=amount
            
            print(f"{amount} is withdrawn, available balance is {self.balance}")
            
    def get_balance(self):
        return self.balance
    
account=BankAccount("bhargav",1000)
print(account.balance)
account.deposit(100)

account.withdraw(200)
account.get_balance()

'''





        
