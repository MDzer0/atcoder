N = int(input())
aLst = []
ans = -1
cnt = 0
for i in range(N):
    aLst.append(int(input()) - 1)

tmp = 0
index = 0
for i in range(N):
    tmp = aLst[tmp]
    aLst[index] = 0
    if tmp == 0:
        break
    elif tmp == 1:
        cnt += 1
        ans = cnt
        break
    else:
        index = tmp
        cnt += 1

print(ans)
