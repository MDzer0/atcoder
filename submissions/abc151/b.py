N, K, M = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
total = sum(a)
if N * M - total > K:
    ans = -1
else:
    if N * M - total < 0:
        ans = 0
    else:
        ans = N * M - total
print(ans)
