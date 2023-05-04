import math
N, D = map(int, input().split())
nlist = []
anslist = []
for i in range(N):
    llist = list(map(int, input().split()))
    nlist.append(llist)
a = 0
for x in range(N - 1):
    for i in range(x, N - 1):
        tmp = 0
        for j in range(D):
            tmp += (abs(nlist[x][j] - nlist[i + 1][j]) ** 2)
        anslist.append(int(math.sqrt(tmp)) - math.sqrt(tmp))

cnt = 0
for i in anslist:
    if i == 0.0:
        cnt += 1
print(cnt)
