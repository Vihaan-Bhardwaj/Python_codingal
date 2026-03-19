from tkinter import *
from PIL import Image, ImageTk

t = Tk()
t.title("Image viewer")
#t.resizable(True, True)
t.geometry("400x400")
upload = Image.open("pexels-gra-wal-38714864-7509250.jpg")
image = ImageTk.PhotoImage(upload)
#image = image.resize((300, 200))
label = Label(t, image=image)
label.place(x=50, y=0)
label.pack()
label2 = Label(t, text="Always stand out")
label2.place(x=40, y=360)
label2.pack()

t.mainloop()