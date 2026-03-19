import tkinter as tk
import random

t = tk.Tk()
t.title("RPS Game")
t.geometry("500x500")
choices = ["Rock", "Paper", "Scissors"]



def play(player_choice):

    choice = random.choice(choices)


    if (player_choice == "Rock" and choice == "Scissors" or 
       player_choice == "Paper" and choice == "Rock" or
       player_choice == "Scissors" and choice == "Paper"):
       lw = tk.Label(t, text="You win!")
       lw.pack(side="bottom") 
    elif  (player_choice == "Rock" and choice == "Paper" or 
           player_choice == "Paper" and choice == "Scissors" or
           player_choice == "Scissors" and choice == "Rock"):
        ll = tk.Label(t, text="You lost")
        ll.pack(side="bottom")
    else:
        ld = tk.Label(t, text="Draw")
        ld.pack()



rb = tk.Button(t, text="Rock", command=lambda: play("Rock"))
pb = tk.Button(t, text="Paper", command=lambda: play("Paper"))
sb = tk.Button(t, text="Scissors", command=lambda: play("Scissors"))
rb.pack()
pb.pack()
sb.pack()

t.mainloop()