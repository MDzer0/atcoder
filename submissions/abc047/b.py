W, H, N = map(int, input().split())

w1 = 0
w2 = W
h1 = 0
h2 = H
ans = 0
tLst = [list(map(int, input().split())) for i in range(N)]

for i in range(N):
    if tLst[i][2] == 1:
        w1 = max(w1, tLst[i][0])
    elif tLst[i][2] == 2:
        w2 = min(w2, tLst[i][0])
    elif tLst[i][2] == 3:
        h1 = max(h1, tLst[i][1])
    elif tLst[i][2] == 4:
        h2 = min(h2, tLst[i][1])

w = w2 - w1
h = h2 - h1
if w <= 0 or h <= 0:
    ans = 0
else:
    ans = int(w * h)
print(ans)
