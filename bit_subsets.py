def bit_subsets(arr):
    n = len(arr)
    return [[arr[j] for j in range(n) if i & (1 << j)] for i in range(1 << n)]

arr = list(map(int, input().split()))
for s in bit_subsets(arr):
    print(s)