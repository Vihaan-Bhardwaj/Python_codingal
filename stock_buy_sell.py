def profit(n):
    prices = list(range(n, 0, -1)) + list(range(1, n+1))
    min_price, profit = prices[0], 0
    for p in prices[1:]:
        min_price = min(min_price, p)
        profit = max(profit, p - min_price)
    return profit

input("maxprofit(n) finds the  best single buy sell price in [n..1, 1..n] Press enter")

print(profit(4))
print(profit(5))

n = int(input("Enter a number (please try 6/7): "))
guess = input("What is max_profit("+ str(n) +")? ")
input("track min price so far sell when gap beats current best price now press enter")
print(f"profit({n}) = {profit(n)}, your guess: {guess}")