N, M = map(int, input().split())
alist = [list(map(int, input().split())) for _ in range(N)]
anslist = [] * M
for i in range(M):
    anslist.append([i + 1, 0])
for i in range(N):
    for j in range(M):
        if alist[i][j] == 1:
            anslist[j][1] += 1
anslist.sort(key=lambda x: x[1], reverse=True)

for i in range(M):
    if i != M - 1:
        print(anslist[i][0], end=' ')
    else:
        print(anslist[i][0])
