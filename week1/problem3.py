s = input("enter string in quotes \n")
longestString = s[0]
sampleString = s[0]

for char in s[1:] :
  if char >= sampleString[-1] :
    sampleString += char 
    if len(sampleString) > len(longestString) :
      longestString = sampleString
  else :
    sampleString = char

print("Longest substring in alphabetical order is: " + longestString) 

  
