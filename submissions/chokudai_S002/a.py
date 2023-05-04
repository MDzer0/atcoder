n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

for ai, bi in ab:
	print(ai * bi)
