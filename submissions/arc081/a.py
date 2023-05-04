from collections import defaultdict
N = int(input())
a = list(map(int, input().split()))
d = defaultdict(int)
ans = 0
for i in a:
    d[i] += 1
ans1 = []
for v, c in d.items():
    if c >= 2:
        ans1.append(v)

ans1.sort(reverse=True)
if len(ans1) > 1:
    ans = ans1[0] * ans1[1]

ans2 = []
for v, c in d.items():
    if c >= 4:
        ans2.append(v)

ans2.sort(reverse=True)

if len(ans2) > 0:
    ans = max(ans, ans2[0] * ans2[0])

print(ans)
