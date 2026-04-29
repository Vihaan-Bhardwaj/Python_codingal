big = int(input("Enter a big number: "))
small = int(input("Enter a small number: "))

while(small):
    ns = small
    small = big % small
    big = ns

print("HCF is: ", big)