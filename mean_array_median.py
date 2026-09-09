def arraymean(arr, arsize):
    total_sum = 0
    for i in range(0, arsize):
        total_sum += arr[i]
    return float(total_sum / arsize)

def arraymedian(arr, arsize):
    sorted(arr)
    if arsize % 2 != 0 :
        return float(arr[int(arsize/2)])
    return float((arr[int((arsize-1)/2)] + arr[int(arsize/2)])/2.0)


arr = [1, 4, 5, 2, 5, 8, 5, 2, 6, 8]
arsize = len(arr)

print("mean = ", arraymean(arr, arsize))
print("median = ", arraymedian(arr, arsize))