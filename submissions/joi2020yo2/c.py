def f(x):
    res = x
    while x > 0:
        res += x % 10
        x //= 10
    return res

N = int(input())
dp = [False for _ in range(10 ** 7)]
dp[N] = True

for i in range(N, 0, -1):
    if dp[f(i)]:
        dp[i] = True

ans = 0
for i in dp:
    if i:
        ans += 1

print(ans)
