def hanoi(n):
    if n == 0:
        return 0
    return 2 * hanoi(n-1) + 1

input("hanoi(n) counts the minimum moves to shift n discs from Peg A to Peg C...... this presentation has ended please press the big enter key")
print(hanoi(1))
print(hanoi(2))
n = int(input("Enter number of discs(try 3/4 it will turn out good)"))
guess = input("what is hanoi("+ str(n) +")? ")
input("hanoi(n) = 2 * hanoi(n-1) + 1 move the stack twice plus the big disk once........ this préséntátíón is now over please press éntré to continue")
print("hanoi(" + str(n) +") = ", hanoi(n), "your guess: ", guess)