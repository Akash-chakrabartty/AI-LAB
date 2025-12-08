# File: compare_memory_and_division.py

# Assign two integer variables
a = 25
b = 10

# Print the variables
print("Value of a:", a)
print("Value of b:", b)

# Compare memory locations using id()
print("\nMemory address of a:", id(a))
print("Memory address of b:", id(b))

if id(a) == id(b):
    print("Both variables have SAME memory location.")
else:
    print("Variables have DIFFERENT memory locations.")

# Perform division operations
float_division = a / b        # floating point division
integer_division = a // b     # integer division

print("\nFloating point division (a / b):", float_division)
print("Integer division (a // b):", integer_division)
