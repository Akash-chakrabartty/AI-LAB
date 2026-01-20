
n = int(input("Enter a 3-digit number: "))


last = n % 10                
middle = (n // 10) % 10      
first = n // 100             

reverse = (last * 100) + (middle * 10) + first

print("Original number:", n)
print("Reversed number:", reverse)
