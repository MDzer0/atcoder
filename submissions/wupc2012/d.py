N = int(input())
sankaku = [[0] * N for _ in range(N)]
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(len(tmp)):
        sankaku[i][j] = tmp[j]
dp = [[0] * N for _ in range(N + 1)]
if N == 1:
    print(sankaku[0][0])
    exit()

for i in range(N):
    for j in range(N - 1):
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + sankaku[i][j])
        dp[i + 1][j + 1] = dp[i][j] + sankaku[i][j + 1]
print(max(dp[N]))
