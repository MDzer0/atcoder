N, M = map(int, input().split())
if M == 0:
    print(1)
    exit()

if N == M:
    print(0)
    exit()

a = list(map(int, input().split()))
a.sort()

cnt = M
kyori = []
if a[0] != 1:
    kyori.append(a[0] - 1)

for i in range(1, M):
    tmp = a[i] - a[i - 1]
    if tmp == 1: continue
    kyori.append(tmp - 1)

if a[-1] != N:
    kyori.append(N - a[-1])

minkyori = min(kyori)
cnt = 0
for i in kyori:
    m, d = divmod(i, minkyori)
    cnt += m
    if d != 0:
        cnt += 1

print(cnt)
