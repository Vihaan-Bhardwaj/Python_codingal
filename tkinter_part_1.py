from tkinter import *

window = Tk()
window.title("Tkinter Sample window")
greeting = Label(text = "Hello user", fg = "black", bg = "white")
button = Button(text = "Click me", bg = "white", fg = "black")
entry = Entry(fg="yellow", bg="blue", width=50)
greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window, relief="ridge", borderwidth=5)
frame.pack()
textbox = Text(fg="green", bg="yellow")
textbox.pack()

window.mainloop()