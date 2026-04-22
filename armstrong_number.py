number = int(input("Enter users number here: "))
digits = len(str(number))
result = 0
temp = number
while temp > 0:
    digit = temp % 10
    result += digit ** digits
    temp //= 10

if number == result:
    print("Armstrong number")
else:
    print("Not an armstrong number")