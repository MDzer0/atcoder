from collections import defaultdict

N = int(input())
A = [int(input()) for _ in range(N)]
d = defaultdict(int)
for i in A:
    d[i] += 1

ans = 0
for v in d.values():
    if v > 1:
        ans += ((v - 1) * v) // 2

print(ans)
