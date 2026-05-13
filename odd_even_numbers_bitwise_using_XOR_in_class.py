def isevenodd(n):
    if n ^ 1 == n+1:
        return True
    else:
        return False

n = int(input("Enter a number :  "))
if isevenodd(n):
    print("EVEN")
else:
    print("ODD")