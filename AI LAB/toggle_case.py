

ch = input("Enter an alphabet: ")

if len(ch) != 1 or not ch.isalpha():
    print("Please enter a SINGLE alphabet only.")
else:
    if ch.islower():
        opposite = ch.upper()
    else:
        opposite = ch.lower()

    print("Original character:", ch)
    print("Opposite case character:", opposite)
