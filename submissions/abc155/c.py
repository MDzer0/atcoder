from collections import defaultdict
N = int(input())
s = [input() for _ in range(N)]
d = defaultdict(int)
for i in s:
    d[i] += 1

dsort = sorted(d.items(), key=lambda x : x[1], reverse=True)
ans = []
tmp = dsort[0][1]
for i, v in dsort:
    if tmp == v:
        ans.append(i)

ans.sort()
for i in ans:
    print(i)
