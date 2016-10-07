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


def calcAnnualBalance(principal, rate, monthlyPayment):
  """
  Calculates the balance after a year of fixed monthly payments 

  principal -- The starting balance in the account

  rate -- The annual interest rate 
  
  monthlyPayment -- The monthly payment
  """
  
  for i in range (0, 12):
    principal = calcMonthlyBalance (principal, rate, monthlyPayment)
  return principal 

if __name__ == "__main__":
  closeEnough = -1.00

  principal = float(input('Enter principal: '))
  annualInterestRate = float(input('Enter annual interest rate: '))

  paymentGuess = principal/6
  lowPaymentGuess = principal/12
  highPaymentGuess = principal
  endOfYearBalance = calcAnnualBalance(principal, annualInterestRate, paymentGuess)
  while (endOfYearBalance < closeEnough) or (endOfYearBalance > 0):
    # print("With payment of %.2f, balance is %.2f" % (paymentGuess, endOfYearBalance))
    # print("Low: %.2f    High: %.2f" % (lowPaymentGuess, highPaymentGuess))
    if endOfYearBalance > 0.00:
      # increase payment guess
      lowPaymentGuess = paymentGuess
      paymentGuess += (highPaymentGuess - paymentGuess)/2
    else :
      # lower payment guess
      highPaymentGuess = paymentGuess
      paymentGuess -= (paymentGuess - lowPaymentGuess)/2
    endOfYearBalance = calcAnnualBalance(principal, annualInterestRate, paymentGuess)
    # input()
  print ( "Lowest Payment: %.2f" % paymentGuess)

