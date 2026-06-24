items = ["A", "B", "C"]
n = len(items)
total = 2 ** n
print("=======POWER MAP=======")
print(f"Items, : {items}")
print("Elements: ", n, "total subsets 2 ^ , ", n, "= ", total)
print()
print("Mask table: ( n = ", n, ") :")
mask = 0
while mask < total:
    bit2 = (mask >> 2)&1
    bit1 = (mask >> 1)&1
    bit0 = mask&1
    print("Mask ", mask , " -> [C][B][A] = ", bit2, bit1 , bit0)
    mask = mask + 1
print()
print("All subsets(bitprobe): ")
mask = 0
while mask < total:
    subset =[]
    j = 0
    while j < n:
        probe = 1 << j
        if (mask & probe) > 0:
            subset.append(items[j])
        j = j + 1
    print("mask", mask, " ->", subset)
    mask = mask + 1
print()