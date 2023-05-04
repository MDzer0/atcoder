from collections import defaultdict

N = int(input())
d = defaultdict(int)

for i in range(N):
    d[int(input())] += 1

ans = 0
for i, j in d.items():
    if j % 2 != 0:
        ans += 1

print(ans)
