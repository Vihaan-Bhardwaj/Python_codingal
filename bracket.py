def cp(n, l=0, r=0):
    if l == n and r == n:
        return 1
    total=0
    if l > r:
        total += cp(n, l, r + 1)
    if l < r:
            total += cp(n, l + 1, r)
    return total

input("Just press enter im in a rush....")
