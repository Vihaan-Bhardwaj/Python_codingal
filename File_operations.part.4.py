new_fiel = open("New.txt", "x")
new_fiel.close()

import os
print("Opening checker code to see if this file exists and restarting hubub")
if os.path.exists("New.txt"):
    os.remove("New.txt")
else:
    print("After running the checker code and restarting hubub, we are sure that this spontaneous file has never been in existence on this laptop, space or the universe (i.e. it doesn't exist)")

r = open("up_cod.txt", "w")
r.write("Hi I am Pengiun again and i am still 1 day old forever")
r.close()

os.remove("up_cod.txt")
os.rmdir("dummy")