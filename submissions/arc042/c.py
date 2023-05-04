N, P = map(int, input().split())
okashi = []
for i in range(N):
    a, b = map(int, input().split())
    okashi.append((a, b))
okashi.sort(reverse=True)

dp =[0 for _ in range(P + 1)]
ans = 0
for i in range(N):
    dp2 = dp[:]
    for j in range(P + 1):
        if j - okashi[i][0] >= 0:
            dp[j] = max(dp2[j], dp2[j - okashi[i][0]] + okashi[i][1])
        else:
            dp[j] = dp2[j]
    for j in range(i + 1, N):
        ans = max(ans, dp[P] + okashi[j][1])
print(ans)
