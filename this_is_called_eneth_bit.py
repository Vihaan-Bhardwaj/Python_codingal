def srn(number, n):
    if number & (1 << (n-1)):
        print("SET")
    else:
        print("NOT SET BECAUSE APPARANTLY THE IF LOOP DECIDED... yea thaz how python goes")

a = int(input("Enter decimal number cos i say so: "))
b = int(input("Enter a bit number (made of ONLY 1s n 0s): "))
srn(a, b)