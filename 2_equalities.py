def issame(n1, n2):
    if ((n1 ^ n2) != 0):
        print("Not equal")
    else:
        print("Equal")

n1 = int(input("Enter num: "))
n2 = int(input("Enter num2: "))
issame(n1, n2)