# File: number_base_conversion.py

num = int(input("Enter a decimal number: "))

print("Choose conversion:")
print("1) Binary")
print("2) Octal")
print("3) Hexadecimal")

choice = int(input("Enter your choice (1-3): "))

match choice:
    case 1:
        # bin() returns string like '0b1010', so we skip first 2 chars
        print("Binary:", bin(num)[2:])
    case 2:
        print("Octal:", oct(num)[2:])
    case 3:
        print("Hexadecimal:", hex(num)[2:].upper())
    case _:
        print("Invalid choice!")

