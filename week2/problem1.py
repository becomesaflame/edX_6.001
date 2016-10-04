"""
balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

output example: Remaining balance: 813.41


math:
Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
"""

def calcMonthlyBalance (principal, rate, minPaymentRate):
  """
  Calculates the updated balance after a minimum monthly payment 

  principal -- The starting balance in the account

  rate -- The annual interest rate 
  
  minPaymentRate -- The minimum monthly payment rate

  """
  minPayment = minPaymentRate * principal
  principal = principal - minPayment
  return principal + rate/12 * principal

balance = float(input('Enter balance: '))
annualInterestRate = float(input('Enter annual interest rate: '))
monthlyPaymentRate = float(input('Enter monthly payment rate: '))

for i in range (0, 12):
  balance = calcMonthlyBalance (balance, annualInterestRate, monthlyPaymentRate)
  # print("Month %i balance: %.2f" % (i, balance)) 
print("Remaining balance: %.2f" % balance)  
