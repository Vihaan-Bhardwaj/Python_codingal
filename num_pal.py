num = int(input("Enter a number: "))
on = num
rn = 0
while num > 0:
    digit = num % 10
    rn = rn * 10 + digit
    num //= 10

if on == rn:
    print(f"{on} is a palindrome")
else:
    print(f"{on} is not a palindrome")