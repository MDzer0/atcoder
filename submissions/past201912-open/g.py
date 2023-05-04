N = int(input())
alst = [list(map(int, input().split())) for _ in range(N - 1)]
nlst = [0] * N
ans = -10 ** 18
def dfs(n):
    global ans
    if n == N:
        tmp = 0
        glst = []
        g1 = []
        g2 = []
        g3 = []
        for i in range(N):
            if nlst[i] == 0:
                g1.append(i)
            elif nlst[i] == 1:
                g2.append(i)
            else:
                g3.append(i)
        glst.append(g1), glst.append(g2), glst.append(g3)
        for i in range(3):
            if glst[i] == [] or len(glst[i]) == 0:
                continue
            for j in range(len(glst[i])):
                for k in range(len(glst[i])):
                    if glst[i][j] < glst[i][k]:
                        tmp += alst[glst[i][j]][glst[i][k] - glst[i][j] - 1]
        ans = max(ans, tmp)
        return

    for i in range(3):
        nlst[n] = i
        dfs(n + 1)

dfs(0)
print(ans)
