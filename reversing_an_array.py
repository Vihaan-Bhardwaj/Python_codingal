def reverse(n):
    arr, i, j = list(range(1, n + 1)), 0, n - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1; j-= 1
    return arr

input("builds  1...n and flips it endtoend using 2 pointers now press enter at the end of this message please...................")
print(reverse(4))
print(reverse(5))
n = int(input("Enter list size try (6 OR 7): "))
guess = input("What is reverse? ")
input("press enter")
print(f"reverse{str(n)} = {reverse(n)} your guess : {guess}")
