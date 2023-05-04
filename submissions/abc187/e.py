import sys
sys.setrecursionlimit(10**6)

N = int(input())
ki = [[] for _ in range(N)]
alist = [-1] * (N - 1)
blist = [-1] * (N - 1)
deepList = [-1] * N
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    ki[a].append(b)
    ki[b].append(a)
    alist[i] = a
    blist[i] = b

deepList[0] = 0
q = [0]
while q:
    n = q.pop()
    for i in ki[n]:
        if deepList[i] == -1:
            deepList[i] = deepList[n] + 1
            q.append(i)

imos = [0] * N
Q = int(input())
for i in range(Q):
    t, e, x = map(int, input().split())
    e -= 1
    va = 0
    vb = 0

    if t == 1:
        va = alist[e]
        vb = blist[e]
    else:
        va = blist[e]
        vb = alist[e]
    if deepList[va] < deepList[vb]:
        imos[0] += x
        imos[vb] -= x
    else:
        imos[va] += x

q = [0]
while q:
    t = q.pop()
    for i in ki[t]:
        if deepList[i] > deepList[t]:
            imos[i] += imos[t]
            q.append(i)

for i in imos:
    print(i)
