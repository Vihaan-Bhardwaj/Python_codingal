n1 = int(input("Enter a number:"))
n2 = int(input("Enter a number: "))
max_num = max(n1, n2)
while True:
    if max_num % n1 == 0 and max_num % n2 == 0:
        print("LCM is: ", max_num)
        break
    max_num += 1