N = int(input())
A = list(map(int, input().split()))
g = [[] for _ in range(N + 1)]
dp = [0] * (N + 1)

for i in range(N - 1):
    g[A[i]].append(i + 2)

for i in reversed(range(1, N + 1)):
    dp[i] = 0
    for j in g[i]:
        dp[i] += dp[j] + 1
print(*dp[1:])
