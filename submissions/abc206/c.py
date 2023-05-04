from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))

d = defaultdict(int)
for i in A:
    d[i] += 1
ans = (N * (N - 1)) // 2
cnt = 0
for v, k in d.items():
    if k != 1:
        cnt += (k * (k - 1)) // 2

print(ans - cnt)
