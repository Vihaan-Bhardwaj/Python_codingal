print("=======Reverse Lab=========")
print()
n = int(input("Enter a number: "))
temp = n
while temp > 0:
    print("    last digit:", temp % 10, "    remaining:", temp // 10)
    temp = temp // 10
print()

def flipnum(num):
    if num // 10 == 0:
        return num
    last = num % 10
    rest = flipnum(num // 10)
    return last * pow(10, len(str(rest))) + rest

n2 = int(input("Enter a number to be flipped: "))
print(n2, "flipped ->", flipnum(n2))
print()

def flipName(s):
    if len(s) == 1:
        return s
    return flipName(s[1:]) + s[0]
name = input("Enter your name to be flipped: ")
print(name, "->", flipName(name))
print()

def ispower4(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 4 == 0:
        return ispower4(n // 4)
    return False

print("16 -> ", ispower4(16), "12 ->", ispower4(12))
guess = int(input("Test your own number!: "))
print(guess, "-> Power of 4?", ispower4(guess))