def f3(n):
    sum = 0
    for i in range(1, n+1):
        for j in range(1, i+1):
            sum += 1
    return sum
print(f3(4))