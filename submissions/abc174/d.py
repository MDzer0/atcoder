N = int(input())
c = input()
rlist = []
wlist = []
for i in range(N):
    if c[i] == 'R':
        rlist.append(i)
    else:
        wlist.append(i)

cnt = 0
if len(rlist) == 0:
    print(0)
    exit()
for i in range(len(wlist)):
    if wlist[i] < rlist[-cnt - 1]:
        cnt += 1
    else:
        break
print(cnt)
