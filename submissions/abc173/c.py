import copy
H, W, K = map(int, input().split())
c = [list(input()) for _ in range(H)]

hlst = [0] * H
wlst = [0] * W
looph = []
loopw = []
def dfs(cnt, lst, loop):
    if cnt == len(lst):
        loop.append(copy.deepcopy(lst))
        return
    for i in range(2):
        lst[cnt] = i
        cnt += 1
        dfs(cnt, lst, loop)
        cnt -= 1

dfs(0, hlst, looph)
dfs(0, wlst, loopw)

total = 0
for i in looph:
    for j in loopw:
        cnt = 0
        for k in range(H):
            for l in range(W):
                if i[k] == 1:
                    continue
                if j[l] == 1:
                    continue
                if c[k][l] == '#':
                    cnt += 1

        if cnt == K:
            total += 1

print(total)
