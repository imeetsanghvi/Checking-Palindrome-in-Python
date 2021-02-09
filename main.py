def checkPalindrome(inputString):
    inputString = inputString.lower()
    rev = reversed(inputString)
    if list(inputString) == list(rev):
        print(True)
    else:
        print(False)

#tesing conditions to be passed
checkPalindrome(input('Enter the string to check for palindrome'))