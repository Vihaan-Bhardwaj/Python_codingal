c = open("Codingal.txt", "r")
print(c.read())
c.close()

c = open("Codingal.txt", "r")
print("\nRead in parts\n")
print(c.read(8))
c.close()

c = open("Codingal.txt", "a")
c.write("Hi, I am penguin and I am 1 year old")
c.close()