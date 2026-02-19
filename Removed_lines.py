f1 = open("Codingal.txt", "r")
f2 = open("up_cod.txt", "w")

for i in f1.readlines():
    if not (i.startswith("Coding")):
        print(i)
        f2.write(i)

f1.close()
f2.close()