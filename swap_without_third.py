# File: swap_without_third.py

# Input two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("\nBefore swapping:")
print("a =", a)
print("b =", b)

# Swap using single statement (mathematical method)
a = a + b; b = a - b; a = a - b

print("\nAfter swapping:")
print("a =", a)
print("b =", b)
