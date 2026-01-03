if 1 == 0:
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
# hari code
n = int(input())
arr = []
for i in range(n):
	arr.append(input().strip())
if len(set(arr)) == len(arr):
	cnt = 1
else:
	pos = -1
	# Try every color each time and whatever gets u the furthest 
	# stick with that don't need to store the color just a while loop
	cnt = 0
	while pos != n - 1:
		blue = 0
		orange = 0
		pink = 0
		green = 0
		red = 0
		yellow = 0
		if 'Blue' in arr[pos + 1:]:
			blue = arr.index('Blue', pos + 1)
		if 'Orange' in arr[pos + 1:]:
			orange = arr.index('Orange', pos + 1)
		if 'Pink' in arr[pos + 1:]:
			pink = arr.index('Pink', pos + 1)
		if 'Green' in arr[pos + 1:]:
			green = arr.index('Green', pos + 1)
		if 'Red' in arr[pos: + 1]:
			red = arr.index('Red', pos + 1)
		if 'Yellow' in arr[pos + 1:]:
			yellow = arr.index('Yellow', pos + 1)
		pos = max(blue, orange, pink, green, red, yellow)
		cnt += 1
print(cnt)