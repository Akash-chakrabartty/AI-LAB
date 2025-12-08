# File: reverse_3digit.py

# Input a 3-digit number
n = int(input("Enter a 3-digit number: "))

# Extract digits using operators
last = n % 10                # unit digit
middle = (n // 10) % 10      # tens digit
first = n // 100             # hundreds digit

# Form the reverse number
reverse = (last * 100) + (middle * 10) + first

# Display result
print("Original number:", n)
print("Reversed number:", reverse)
