N, K = map(int, input().split())
a = list(map(int, input().split()))
dp = [False] * (N + 1)

for i in range(N + 1):
    for j in a:
        if i >= j and dp[i - j] == False:
            dp[i] = True

if dp[N]:
    print('First')
else:
    print('Second')
