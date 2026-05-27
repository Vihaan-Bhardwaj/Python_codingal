num = int(input("Enter a number: "))
binary = bin(num)[2:]
reverseb = binary[::-1]
new = int(reverseb, 2)
print("Original: ", num)
print("BInary: ", binary)
print("Reversed: ", reverseb)
print("New: ", new)