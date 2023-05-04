N = int(input())
wlst = [input() for i in range(N)]
wset = set(wlst)
if len(wset) != N:
    print('No')
    exit()

tmp = wlst[0][-1]
for i in range(1, N):
    if tmp != wlst[i][0]:
        print('No')
        exit()
    tmp = wlst[i][-1]

print('Yes')
