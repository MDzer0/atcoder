N, H = map(int, input().split())
ablst = [list(map(int, input().split())) for _ in range(N)]
ablst.sort(key=lambda x: x[0])
amax = ablst[-1][0]
ablst.sort(key=lambda x: x[1], reverse=True)
blst = []
for i in range(N):
    if amax <= ablst[i][1]:
        blst.append(ablst[i][1])
    else:
        break

cnt = 0
for i in blst:
    H -= i
    cnt += 1
    if H <= 0:
        break

if H <= 0:
    print(cnt)
else:
    acnt = H // amax
    cnt += acnt
    if H - (amax * acnt) <= 0:
        print(cnt)
    else:
        print(cnt + 1)
