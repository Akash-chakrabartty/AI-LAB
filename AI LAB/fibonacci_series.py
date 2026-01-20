# File: fibonacci_series.py

n = int(input("Enter number of terms: "))

if n <= 0:
    print("Please enter a positive number.")
else:
    a = 0
    b = 1
    print("Fibonacci series:")

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

    print()  # new line
