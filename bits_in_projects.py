def rmsb(n):
    result = n & -n
    print("Rightmost set bit is ", result)


n = int(input("Enter a number: "))
rmsb(n)