n = int(input())
possible = ["Blue", "Orange", "Pink", "Green", "Red", "Yellow"]
seen = []
best = []
count = 0
for _ in range(n):
    inp = input()
    if inp not in seen:
        seen.append(inp)
    else:
        count += 1
    if len(seen) == len(possible):
        seen = []
        best.append(inp)
        count = 0
print(len(best) + count + (1 if seen else 0))
