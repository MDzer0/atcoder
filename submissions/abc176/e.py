H, W, M = map(int, input().split())
hlist = [0] * H
wlist = [0] * W
hw = set()
for i in range(M):
    h, w = map(int, input().split())
    hlist[h - 1] += 1
    wlist[w - 1] += 1
    hw.add((h - 1, w - 1))

hmax = max(hlist)
wmax = max(wlist)
hmaxlist = [i for i, v in enumerate(hlist) if v == hmax]
wmaxlist = [i for i, v in enumerate(wlist) if v == wmax]
cnt = -1
for i in hmaxlist:
    bf = False
    for j in wmaxlist:
        if not (i, j) in hw:
            cnt = 0
            bf = True
            break
    if bf:
        break

print(hmax + wmax + cnt)
