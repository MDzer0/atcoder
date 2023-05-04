from collections import defaultdict
N = int(input())
A = list(map(int, input().split()))
d = defaultdict(int)

for i in A:
    d[i] += 1
ans = 0
for v in d.values():
    if v >= 3:
        ans += (v * (v - 1) * (v - 2)) // 6

print(ans)
