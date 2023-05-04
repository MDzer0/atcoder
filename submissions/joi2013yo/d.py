INF = 10 ** 9 + 7
D, N = map(int, input().split())
T = [int(input()) for i in range(D)]
abc = [list(map(int, input().split())) for _ in range(N)]
koho = [[] for _ in range(D)]
dp = [[-1] * 2 for _ in range(D)]
keisan = [[-1, -1] for _ in range(D)]

for i in range(D):
    for j in range(N):
        if abc[j][0] <= T[i] <= abc[j][1]:
            koho[i].append(abc[j][2])

for i in range(D):
    keisan[i][0] = min(koho[i])
    keisan[i][1] = max(koho[i])
dp[0][0] = 0
dp[0][1] = 0

for i in range(D - 1):
    for j in range(2):
        for k in range(2):
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][k] + abs(keisan[i][k] - keisan[i + 1][j]))

print(max(dp[D - 1]))
