def group_reverse(n):
    arr = [1, 2, 3, 4, 5, 6]
    for i in range(0, 6, n):
        arr[i:i+n] = arr[i:i+n][::-1]
    return arr

input("ENTER")
print(group_reverse(2))
print(group_reverse(3))
n = int(input("Size: (1-6): "))
guess = input("What is gr.????? ")
print("Group reverse = ", group_reverse(n), "ur guess:", guess)