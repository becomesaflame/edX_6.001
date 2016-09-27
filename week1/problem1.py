s = input()
numVowels = 0
vowels = ['a','e','i','o','u']
for char in s:
  if char in vowels:
    numVowels += 1
print (numVowels)
