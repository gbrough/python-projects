# Ask user for input string
# Reverse the string
# compare if string is equal
# challenge - use functions
word = None

def wordInput():
  word = input("Please type a word you would like to see if it's a palindrome\n").lower()
  return word

def reverseWord():
  reversedWord = word[::-1]
  return reversedWord

def palindromeCheck():
  if word == reverseWord:
    print("Yes, you have entered a palindrome")
  else:
    print("Sorry, this word is not a palindrome")

def main():
  print("\nPalindrome Checker")
  wordInput
  reverseWord
  palindromeCheck

main()