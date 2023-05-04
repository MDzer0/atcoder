N = int(input())
h = list(map(int, input().split()))
dp = [0] * N
dp[1] = abs(h[0] - h[1])

for i in range(2, N):
    dp[i] = min(dp[i - 1] + abs(h[i - 1] - h[i]),
                dp[i - 2] + abs(h[i - 2] - h[i]))
ans = []
tmp = N

while True:
    ans.append(tmp)
    if tmp == 1: break

    if dp[tmp - 1] - abs(h[tmp - 1] - h[tmp - 2]) == dp[tmp - 2]:
        tmp -= 1
    else:
        tmp -= 2
print(len(ans))
print(*reversed(ans))
