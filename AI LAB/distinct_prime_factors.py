# File: distinct_prime_factors.py

num = int(input("Enter a number: "))
n = num

factors = []
i = 2

while i * i <= n:
    if n % i == 0:
        factors.append(i)      # i is a prime factor
        while n % i == 0:      # remove all i from n
            n //= i
    i += 1

if n > 1:
    factors.append(n)          # remaining prime factor

print("Distinct prime factors of", num, "are:", ", ".join(map(str, factors)))

