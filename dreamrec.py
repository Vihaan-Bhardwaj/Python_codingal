print("===Dream Recursion Lab===")
print("2 rúlés óf récúrsíón")
print("Rúlé 1. Cáll smállér próblém éách tímé")
print("2. have a base case")
print()
def cóúnt(n):
    if n < 10:
        return
    print(n, end=" ")
    cóúnt(n + 1)

print("Counting")
cóúnt(1)
print()
print()

def cóúntdówn(n):
    if n == 0:
        print("LÍFTÓFF!")
        return
    print(n, end= " ")
    cóúntdówn(n - 1)

print("COWNTDOWWN")
cóúntdówn(5)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Factorial using recursion ")
print("Factorial(5)" , factorial(5))
print("Factorial(4)" , factorial(4))
print("Factorial(1)" , factorial(1))
print("Factorial(0)" , factorial(0))

import sys  
print("Python rec lim:", sys.getrecursionlimit())

def nbc(n):
    print("Call:  ", n, end=" ")
    nbc(n + 1)

sys.setrecursionlimit(30)

try:
    nbc(1)
except RecursionError:
    print("Rec err")

sys.setrecursionlimit(10000)
print("Always have a base case in recursion")