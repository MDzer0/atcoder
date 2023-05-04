N, M = map(int, input().split())
d = [int(input()) for i in range(M)]
caseLst = [i for i in range(1, N + 1)]
tmp = 0
for i in range(M):
    if tmp != d[i]:
        index = caseLst.index(d[i])
        caseLst[index] = tmp
        tmp = d[i]
for i in caseLst:
    print(i)
