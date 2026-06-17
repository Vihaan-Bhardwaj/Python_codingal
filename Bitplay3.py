a = 56
b = 12
print("Bitplay 3")
print(f"A = {a} and b = {b}")
a = a+b
b = a-b
a = a-b
print(f"a {a} b {b}")
print()
a = 56
b = 12
a = a ^ b
b = a ^ b
a = a ^ b
print(f"a {a} b {b}")


print("Left shift")
print("3 << 1 = " , 3 << 1)
print("3 << 2 = " , 3 << 2)
print("3 << 3 = " , 3 << 3)
print("3 << 4 = " , 3 << 4)
print("3 << 5 = " , 3 << 5)

def div(a, b):
    neg = (a < 0) ^ (b < 0)
    a = abs(a)
    b = abs(b)
    count = 0
    while a >= b:
        a = a - b
        count = count + 1
    if neg:
        count = -count
    return count

print("Divide without /:")
print("50 / 2 = ", div(50, 2))
print("72 / 3 = ", div(72,3))
print("-50 / 2 = ", div(-50, 2))
print("50 / -2 = ", div(50, -2))
