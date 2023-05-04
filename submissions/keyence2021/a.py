N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if N == 1:
    print(a[0] * b[0])
    exit()
maxa = [0] * N
maxb = [0] * N
tmpa = 0
tmpb = 0
atmp = 0
for i in range(N):
    atmp = max(a[i], atmp)
    maxb[i] = b[i] * atmp

for i in range(N):
    tmpa = max(tmpa, a[0] * b[i])
    maxa[i] = tmpa

ans = [a[0] * b[0]]
ab = 0
tmp = a[0] * b[0]
for i in range(1, N):
    tmp = max(tmp, a[i] * b[i], maxa[i], maxb[i])
    ans.append(tmp)
for i in ans:
    print(i)
