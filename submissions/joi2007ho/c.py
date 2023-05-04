from collections import defaultdict

N = int(input())
d = defaultdict(int)
for i in range(N):
    x, y = map(int, input().split())
    d[(x, y)] += 1

ans = 0
key = list(d.keys())
key.sort()
index = 0
for i in key:
    for j in key[index + 1:]:
        if i != j:
            tmpx = i[0] -j[0]
            tmpy = i[1] - j[1]
            if (i[0] - tmpy, i[1] + tmpx) in d:
                if (j[0] - tmpy, j[1] + tmpx) in d:
                    ans = max(ans, tmpx ** 2 + tmpy ** 2)
            if (i[0] + tmpy, i[1] - tmpx) == 1 in d:
                if (j[0] + tmpy, j[1] - tmpx) in d:
                    ans = max(ans, tmpx ** 2 + tmpy ** 2)
    index += 1

print(ans)
