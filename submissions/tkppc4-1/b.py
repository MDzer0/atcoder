N, K = map(int, input().split())
a = list(map(int, input().split()))
ans = -1
tmp = 0
for i in range(N):
    if a[i] < K:
        if tmp < a[i]:
            ans = i + 1
            tmp = a[i]
print(ans)
