# File: variable_types_demo.py

# Assign different types of values
name = "Akash"          # string
age = 23                # integer
height = 5.11           # float
is_student = True       # boolean
marks = [85, 90, 78]    # list
person = {"city": "BBSR", "year": 2025}  # dictionary
numbers = (1, 2, 3)     # tuple

# Print all variables
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)
print("Marks:", marks)
print("Person:", person)
print("Numbers:", numbers)

print("\n--- Types of Variables ---")
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of is_student:", type(is_student))
print("Type of marks:", type(marks))
print("Type of person:", type(person))
print("Type of numbers:", type(numbers))


print("\nAll variables:", list(globals().keys()))

del age


print("\nAfter deleting 'age':")
try:
    print(age)
except NameError:
    print("Variable 'age' does not exist now!")
