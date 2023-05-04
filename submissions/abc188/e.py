N, M = map(int, input().split())
A = list(map(int, input().split()))
ki = [[] for _ in range(N)]
for i in range(M):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    ki[x].append(y)

ans = -10 ** 10
dp = [10 ** 10] * (N + 1)
for i in range(N):
    ans = max(ans, A[i] - dp[i])
    dp[i] = min(dp[i], A[i])
    for j in ki[i]:
        dp[j] = min(dp[i], dp[j])
print(ans)
