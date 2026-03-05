from tkinter import *

window = Tk()
window.title("Password inputter")
greeting = Label(text="Welcome user \n please enter a password in the black box below")
password = Entry(fg="gray", bg="black", width=400)
click = Button(text="Done", bg="black", fg="gray")
greeting.pack()
password.pack()
click.pack()

window.mainloop()