import bisect
N, K = map(int, input().split())
a = list(map(int, input().split()))
suma = [0] * N
suma[0] = a[0]
for i in range(1, N):
    suma[i] = suma[i - 1] + a[i]

tmp = K
ans = 0
for i in range(N):
    index = bisect.bisect_left(suma, tmp)
    if index != K:
        ans += N - index
    tmp += a[i]

print(ans)
