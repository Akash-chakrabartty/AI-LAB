# File: triangle_check.py

# Input three numbers
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

# Check triangle condition using operators only
if (a + b > c) and (a + c > b) and (b + c > a):
    print(1)
else:
    print(0)
