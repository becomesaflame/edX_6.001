# Paste your code into this box
print("Please think of a number between 0 and 100!")
high = 100
low = 0
guess = 50 
response = ''
while response != 'c' :
  response_string = "Is your secret number " + str(guess) + "?\n" + "Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."
  response = input(response_string)
  if response == 'l' :
    guess = (high - guess) // 2 + guess
    low = guess
  elif response == 'h':
    guess = (guess - low) // 2 + low
    high = guess
  elif response == 'c':
    print("Game over. Your secret number was: " + str(guess))
    break
  else:
    print("Sorry, I did not understand your input.")
  print ("high: " + str(high), end='')
  print ("low: " + str(low),end='')
  print ("guess: " + str(guess),end='')

                                                                                                        

                                                                                                        
