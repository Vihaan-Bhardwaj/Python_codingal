adj = ["red", "healthy", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)


list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]
for i in list1:
    for j in list2:
        if i == j:
            print(i*j)
