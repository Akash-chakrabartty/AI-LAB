# File: biggest_of_two.py

# Input two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Find the biggest number using operators
if a > b:              # using > operator only
    biggest = a
else:
    biggest = b

# Display result
print("The biggest number is:", biggest)
