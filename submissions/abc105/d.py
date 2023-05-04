from collections import defaultdict

N, M = map(int, input().split())
a = list(map(int, input().split()))

tlst = [0] * (N + 1)
tlst[0] = 0
for i in range(1, N + 1):
    tlst[i] = (tlst[i - 1] + a[i - 1]) % M
d = defaultdict(int)
ans = 0
for i in range(N + 1):
    ans += d[tlst[i]]
    d[tlst[i]] += 1

print(ans)
