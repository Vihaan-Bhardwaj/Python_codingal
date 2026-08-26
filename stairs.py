def ways(stairs):
    if stairs < 0:
        return 0
    if stairs == 0:
        return 1
    return ways(stairs - 1) + ways(stairs - 2)

input("ways (a function that I developed) counts every distinct path up N stairs (1 or 2 times)... now press the 'Entré' key in your clavier to continué...")
print(ways(3))
print(ways(4))


n = int(input("try number of steps (do 5 or 6 cos im dev): "))
guess = input("ways guess now(" + str(n) +"): ")
input("Both branches always combine. *click éntré on ton clavier...")
print("ways("+ str(n) +") = ", ways(n), "your guess:", guess)