N, K = map(int, input().split())
a = list(map(int, input().split()))
ans = [0] * N
ans[0] = a[0]
for i in range(1, K):
    ans[i] = ans[i - 1] + a[i]
total = ans[K - 1]
tmp = total
for i in range(K, N):
    tmp = tmp + a[i] - a[i - K]
    total += tmp

print(total)
