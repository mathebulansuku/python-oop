# For this challenge, create a bank account class that has 2 attributes: Owner and balance. 2 Methods: deposit and withdraw. Withdrawal amount should not excedd the available balance.


class Account():
  
  def __init__(self, owner, balance=0):

    self.owner = owner
    self.balance = balance

  def deposit(self,deposited_amount):
    self.balance += deposited_amount

  def withdrawal(self,withdrawal_amount):

    if self.balance >= withdrawal_amount:
      self.balance -= withdrawal_amount
    else:
      print ("Insufficient funds to withdraw requested amount")


  def __str__(self):
    return f"Account owner: {self.owner} Account balance: {self.balance}"
  

myaccount = Account("Nsuku")

print(myaccount.deposit(400))
print(myaccount.withdrawal(300))
print(myaccount)

    