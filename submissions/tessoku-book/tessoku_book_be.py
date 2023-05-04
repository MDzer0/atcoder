N, Q = map(int, input().split())
A = list(map(int, input().split()))
XY = [list(map(int, input().split())) for _ in range(Q)]
dp = [[0] * (N + 1) for _ in range(30)]

for i in range(1, N + 1):
	dp[0][i] = A[i - 1]

for i in range(1, 30):
	for j in range(1, N + 1):
		dp[i][j] = dp[i - 1][dp[i - 1][j]]

for x, y in XY:
	place = x
	for i in reversed(range(30)):
		if y >> i & 1:
			place = dp[i][place]
	print(place)
