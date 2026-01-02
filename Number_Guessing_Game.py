import random

t = [1, 3, 6, 7, 53, 15]
secret = random.choice(t)

print("-------NUMBER GUESSING GAME-------")
print("The judge will secretly guess a number from the list below.\nYou will have to guess what the judge has chosen.")
print(t)
print("The judge has chosen!!!")

user = int(input("Enter your guess: "))

if user < secret:
    print("The judge's number was greater than your guess. He chose: ",secret)
elif user > secret:
    print("The judge's number was less than your guess. He chose: ",secret)    
else:
    print("You guessed the judge's number!!!. He also chose ", secret)   