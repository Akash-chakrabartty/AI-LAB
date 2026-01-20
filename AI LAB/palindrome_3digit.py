# File: palindrome_3digit.py

# Input a 3-digit number
n = int(input("Enter a 3-digit number: "))

# Extract digits using operators only
last = n % 10                # last digit
middle = (n // 10) % 10      # middle digit
first = n // 100             # first digit

# Reverse the number
reverse = (last * 100) + (middle * 10) + first

# Check palindrome
if n == reverse:
    print(n, "is a palindrome number")
else:
    print(n, "is NOT a palindrome number")
