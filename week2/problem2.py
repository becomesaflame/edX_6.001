"""
Pset 2 Problem 2
"""



def calcMonthlyBalance (principal, rate, payment):
  """
  Calculates the updated balance after a fixed monthly payment 

  principal -- The starting balance in the account

  rate -- The annual interest rate 
  
  payment -- The monthly payment
  """
  
  principal = principal - payment
  return principal + rate/12 * principal


def calcAnnualBalance(principal, rate, monthlyPayment)
  """
  Calculates the balance after a year of fixed monthly payments 

  principal -- The starting balance in the account

  rate -- The annual interest rate 
  
  monthlyPayment -- The monthly payment
  """
  
  for i in range (0, 12):
    balance = calcMonthlyBalance (balance, annualInterestRate, monthlyPaymentRate)
  return balance 


principal = float(input('Enter principal: '))
annualInterestRate = float(input('Enter annual interest rate: '))

payment = principal / 2
while (
  calcAnnualBalance(principal, annualInterestRate, payment)


balance = float(input('Enter balance: '))
annualInterestRate = float(input('Enter annual interest rate: '))
monthlyPaymentRate = float(input('Enter monthly payment rate: '))

for i in range (0, 12):
  balance = calcMonthlyBalance (balance, annualInterestRate, monthlyPaymentRate)
  # print("Month %i balance: %.2f" % (i, balance)) 
print("Remaining balance: %.2f" % balance)  
