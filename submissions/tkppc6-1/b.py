from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))

d = defaultdict(int)
for i in A:
    d[i] += 1
ans = min(N, len(d) + M)
print(ans)
