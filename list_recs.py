scores = [340, 120, 410, 85, 270, 190, 55]
print("Part 1")
print(f"leaderboard: {scores}")
print("Head:", scores[0])
print("Tail:", scores[1:])
print("Head of tail:", scores[1:][0])
print("Tail of tail:", scores[1:][1:])

def shrink(a, depth=0):
    indent = "  " * depth
    print(f"{indent}List: {a}  -> length = {len(a)}")
    if len(a) < 1:
        print(f"{indent} Base case reached")
        return
    shrink(a[1:], depth+1)

print()
print("Part 2:")

def is_sorted(a):
    if len(a) <= 1:
        return True
    return a[0] <= a[1] and is_sorted(a[1:])

print("Part 3:")
print("Scores:", scores)
print("Is_sorted(scores)?", is_sorted(scores))
ranked = [55, 85, 120, 190, 270, 340, 410]
print("Ranked scores:", ranked)
print("Is_sorted:", is_sorted(ranked))

def total_score(a):
    if len(a) == 1:
        return a[0]
    return a[0] + total_score(a[1:])

print("Part 4")
print("Score:", scores)
print("total:", total_score(scores))