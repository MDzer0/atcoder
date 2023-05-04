from collections import defaultdict

N = int(input())
a = list(map(int, input().split()))
rui = [0] * (N + 1)
for i in range(N):
    rui[i + 1] = rui[i] + a[i]

d = defaultdict(int)
for key in rui:
    d[key] += 1

sortd = sorted(d.items(), key=lambda x: x[1], reverse=True)

cnt = 0
for i, j in sortd:
    if j >= 2:
        cnt += (j * (j - 1) // 2)
print(cnt)
