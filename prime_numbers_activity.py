from math import sqrt

num = int(input("Enter a number: "))
print("\n")

if num > 1:
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            print(f"After a good old 'for i in range()' loop {num} IS NOT a prime number")
            break
    else:
        print(f"After a good old 'for i in range()' loop {num} IS a prime number")
else:
    print(f"After a good old 'for i in range()' loop {num} IS NOT a prime number")