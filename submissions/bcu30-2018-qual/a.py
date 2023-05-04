from collections import defaultdict

N = int(input())
A = list(map(int, input().split()))
d = defaultdict(int)
for i in range(30):
    d[i] = 0

for i in A:
    d[i] += 1

ans = []
for i in d.values():
    ans.append(i)
print(*ans)
