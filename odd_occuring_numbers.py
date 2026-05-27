def odd(arr):
    res = 0
    for element in arr:
        res = res ^ element
    return res
arr = []
n = int(input("Enter array size spacific to the laptop brand (no lptp means SKIP): "))
while(n):
    num = int(input("Enter number: "))
    arr.append(num)
    n-=1

print("Odd occuting numver ia: ", odd(arr))