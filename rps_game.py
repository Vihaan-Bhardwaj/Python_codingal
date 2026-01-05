import random, sys


print("====================ROCK PAPER SCISSORS====================")
print("First you will choose out of r, p, s, or quit to do an action.")
print("Then the computer(python) will choose ROCK, PAPER or SCISSORS. Good luck!!!")
wins = 0
losses = 0
ties = 0

while True:
    print("%s Wins, %s Losses, %s Ties" % (wins, losses, ties))
    while True:
        print("Enter your action: rock(r), paper(p), scissors(s) or quit(q)")
        player_move = input("> ")
        if player_move == "q":
            print("Thank you for playing...")
            sys.exit()
        if player_move == "r" or "p" or "s":
            break
        print("Type one of r, p, s, or q")

    if player_move == "r":
        print("ROCK verses....")
    if player_move == "p":
        print("PAPER verses....")
    if player_move == "s":
        print("SCISSORS verses....")





    move_number = random.randint(1, 3) 
    if move_number == 1:
         computer_move = 'r'
         print('ROCK')
    elif move_number == 2:
        computer_move = 'p'
        print('PAPER')
    elif move_number == 3:
        computer_move = 's'
        print('SCISSORS')


        
    if player_move == computer_move:
        print('It is a tie!')
        ties = ties + 1
    elif player_move == 'r' and computer_move == 's':
        print('You won!:)')
        wins = wins + 1
    elif player_move == 'p' and computer_move == 'r':
        print('You won!:)')
        wins = wins + 1
    elif player_move == 's' and computer_move == 'p':
        print('You won!:)')
        wins = wins + 1
    elif player_move == 'r' and computer_move == 'p':
        print('You lost:(, Better luck next time!')
        losses = losses + 1
    elif player_move == 'p' and computer_move == 's':
        print('You lost:(, Better luck next time!')
        losses = losses + 1
    elif player_move == 's' and computer_move == 'r':
        print('You lost:(, Better luck next time!')
        losses = losses + 1