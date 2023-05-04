a, b = map(int, input().split())
m = int(input())
mlist = [list(map(int, input().split())) for _ in range(m)]
dp = [[0 for _ in range(a)] for _ in range(b)]
for i in mlist:
    x, y = i[1], i[0]
    dp[-x][y - 1] = -1
dp[b - 1][0] = 1

for i in reversed(range(b)):
    for j in range(a):
        if i - 1 >= 0 and dp[i - 1][j] != -1:
            if dp[i][j] != -1:
                dp[i - 1][j] = dp[i - 1][j] + dp[i][j]
            else:
                dp[i - 1][j] = dp[i - 1][j] + 0
        if j + 1 < a and dp[i][j + 1] != -1:
            if dp[i][j] != -1:
                dp[i][j + 1] = dp[i][j + 1] + dp[i][j]
            else:
                dp[i][j + 1] = dp[i][j + 1] + 0

print(dp[0][a - 1])
