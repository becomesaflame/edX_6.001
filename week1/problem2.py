s = input('enter string')
numBobs = 0
for i in range(2,len(s)) :
#  print(s[i-3:i])
  if s[i-3:i] == "bob" :
    numBobs += 1
print (numBobs) 

