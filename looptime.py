def looptime(n):
    i1 = 0
    print("First Loop")
    for i in range(0,n+1):
        i1 += 1
    print("First iterations:", i1)
    j=1
    j1 = 0
    print("Second Loop ", j)
    while(j<=n+1):
        j = j*2
        j1 += 1
    print("Second iterations:", j1)
    f1 = 0
    print("Third loop")
    for i in range(0,100):
        f1 += 1
    print("Third iterations:", f1)

looptime(21)
looptime(992)
looptime(67)