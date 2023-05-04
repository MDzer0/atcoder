from collections import defaultdict
A = list(map(int, input().split()))
d = defaultdict(int)

for i in A:
    d[i] += 1
print(len(d))
