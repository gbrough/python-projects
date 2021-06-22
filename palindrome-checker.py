# Ask user for input string
# Reverse the string
# compare if string is equal
# challenge - use functions

word = input("Please type a word you would like to see if it's a palindrome\n")
reverseWord = word[::-1]

if word == reverseWord:
  print("Yes, you have entered a palindrome")
else:
  print("Sorry, this word is not a palindrome")
# print(reverseWord)