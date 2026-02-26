with open("up_cod.txt", "w") as r:
    r.write("Hi I am Penguin and I am 1 day old")
r.close()

with open("up_cod.txt", "r") as r:
    data = r.readlines()
    print("Words in this fiel are...")
    for line in data:
        word = line.split()
        print(word)
r.close()