def odd2(arr, size):
    xorof2 = arr[0]
    x = 0
    y = 0
    Setbit = 0
    for i in range(1, size):
        xorof2 = xorof2 ^ arr[i]
    setbit = xorof2 & ~(xorof2 - 1)
    for i in range(size):
        if (arr[i] & setbit):
            x = x ^ arr[i]
        else:
            y = y ^ arr[i]
        print(f"The two odd elements are {x} and {y}")
arr = []
arsize = int(input("ENter array size: "))
for i in range(0, arsize):
    z = int(input("ENter element: "))
    arr.append(z)

odd2(arr, arsize)