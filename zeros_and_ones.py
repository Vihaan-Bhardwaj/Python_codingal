def nob(n):
    o = 0
    z = 0
    while(n):
        if(n&1==1):
            o+=1
        else:
            z+=1
        n >>=1
    print("ONES: ", o, "ZEROS: ", z)

n = int(input("Enter a number: "))
nob(n)