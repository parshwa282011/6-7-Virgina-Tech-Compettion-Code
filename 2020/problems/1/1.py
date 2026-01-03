if __name__ == "__main__":
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
from itertools import zip_longest
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
        # Instead of checking every color every time, we can check 
        # for all indices of all colors, and get the closest index after pos + 1
        cnt = 0
        blue = []
        orange = []
        pink = []
        green = []
        red = []
        yellow = []
        for i in range(n):
                if arr[i] == 'Blue':
                        blue.append(i)
                if arr[i] == 'Orange':
                        orange.append(i)
                if arr[i] == 'Pink':
                        pink.append(i)
                if arr[i] == 'Green':
                        green.append(i)
                if arr[i] == 'Red':
                        red.append(i)
                if arr[i] == 'Yellow':
                        yellow.append(i)
        big = list(zip_longest(blue, orange, pink, green, red, yellow, fillvalue = -1))
        cnt = 0
        g = 0
        while g < n - 1:
                g = max(big[cnt])
                cnt += 1
print(cnt)