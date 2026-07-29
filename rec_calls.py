def linear(n):
    if n == 0:
        return
    print(n, end=" ")
    linear(n - 1)

print("Linear")
linear(5)
print()

def tail(n):
    if n == 0:
        return
    print(n, end=" ")
    tail(n - 1)

print("tail")
tail(5)
print()


def head(n):
    if n == 0:
        return
    print(n, end=" ")
    head(n - 1)

print("head")
head(5)
print()

def ic(n):
    if n == 0:
        return
    print(n, end=" ")
    ic(n - 1)
    print(n, end=" ")

print("incdec")
ic(4)
print()

def tree(n):
    if n == 0:
        return
    print(n, end=" ")
    tree(n - 1)
    tree(n - 1)

print("tree")
tree(3)
print("lvls x2")