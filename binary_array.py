def max_ones(n):
    arr = [1]*n + [0] + [1]*n
    streak = best = 0 
    for x in arr:
        if x : streak += 1
        else: streak = 0
        if streak > best: best = streak
    return best

input("max_ones(n) finds the longest run of 1s in [1..1, 0, 1..1]. Press enter.")

print(max_ones(3))
print(max_ones(4))
n = int(input("Enter n(try 5 or 6): "))
guess = input("What is max_numbers("+ str(n) +")? : ")
input("streak resets to 0 on each 0 - best keeps the highest streak seen press enter....")
print(f"max_ones({str(n)} = {max_ones(n)} your guess : {guess})")