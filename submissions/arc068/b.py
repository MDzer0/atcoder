from collections import defaultdict
N = int(input())
a = list(map(int, input().split()))

d = defaultdict(int)
for i in a:
    d[i] += 1

maxcnt = len(d)
total = 0
for v, c in d.items():
    if c != 1:
        total += c - 1

if total % 2 == 0:
    print(maxcnt)
else:
    print(maxcnt - 1)
