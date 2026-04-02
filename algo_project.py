def f1(n):
    return n*(n+1)/2
def f2(n):
    sum = 0
    for i in range(1, n+1):
        sum+=i
    return sum
print(f1(10))
print(f2(10))