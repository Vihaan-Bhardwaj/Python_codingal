file1 = open("Bob.txt", "a")
print("Bob:")
file1.write("\nMy favourite subject is Math")
file1.close()

f2 = open("Alice.txt", "a")
print("Alice:")
f2.write("My favourite subject is Literacy")
f2.close()

f3 = open("Kieran", "a")
print("Kieran:")
f3.write("My favourite subjct is Python")
f3.close()