from collections import defaultdict

N = int(input())
d = defaultdict(int)
for i in range(N):
    k = int(input())
    s = list(input().split())
    for i in s:
        d[i] += 1

ans = 0
for v in d.values():
    if v == N:
        ans += 1

print(ans)
