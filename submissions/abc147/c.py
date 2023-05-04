N = int(input())
d = [-1] * N
a = []
x = [[0, 0] for _ in range(N)]
cnt = 0
def dfs(v):
    global cnt
    if v == N:
        cntF = True
        for i in range(N):
            if d[i] != 1:
                continue
            for j in range(len(a[i])):
                if a[i][j][1] != d[a[i][j][0] - 1]:
                    cntF = False
                    break
            if cntF == False:
                break

        if cntF:
            cnt = max(cnt, sum(d))
        return

    d[v] = 0
    dfs(v + 1)
    d[v] = 1
    dfs(v + 1)
    return

for i in range(N):
    tmp = int(input())
    tmplst = [[0, 0] for _ in range(tmp)]
    for j in range(tmp):
        x1, y1 = map(int, input().split())
        tmplst[j][0] = x1
        tmplst[j][1] = y1
    a.append(tmplst)
dfs(0)
print(cnt)
