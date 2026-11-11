def eqv(n):
    arr = [1]*n + [n] + [1] * n
    size = len(arr)
    for i in range(size):
        left_sum = 0
        right_sum = 0
        for j in range(i):
            left_sum += arr[j]
        for k in range(i + 1, size):
            right_sum += arr[k]
        if left_sum == right_sum:
            return i
    return -1

n = int(input("Enter n(try 5 or 6)"))
guess = input("What is eqv("+str(n) +")" )
print("eqv(" + str(n) + ") =", eqv(n), "your guess:", guess)