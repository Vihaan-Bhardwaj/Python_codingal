file_read = open('Codingal.txt', 'r')
print("File in read mode ...")
print(file_read.read())
file_read.close()

file_write = open('Codingal.txt', 'w')
file_write.write("File in write mode...")
file_write.write("Hi, I am Penguin. I am 1 year old")
file_write.close()

file_app = open("Codingal.txt", "a")
file_app.write("\nFile in append mode...")
file_app.write("Hi, Penguin here again! I am now 2 years old")
file_app.close()