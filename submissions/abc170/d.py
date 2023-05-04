from collections import defaultdict

N = int(input())
a = list(map(int, input().split()))
anstable = [0] * (10 ** 6 + 1)
d = defaultdict(int)
for i in a:
    d[i] += 1

u = []
for i, v in d.items():
    if v == 1:
        u.append(i)
a = set(a)
for i in a:
    for j in range(i * 2, 10 ** 6 + 1, i):
        anstable[j] += 1

cnt = 0
for i in u:
    if anstable[i] == 0:
        cnt += 1

print(cnt)
