N = int(input())
aLst = list(map(int, input().split()))
zougen = ''

cnt = 0
for i in range(N - 1):
    if zougen == 'U':
        if aLst[i] > aLst[i + 1]:
            cnt += 1
            zougen = ''
    elif zougen == 'D':
        if aLst[i] < aLst[i + 1]:
            cnt += 1
            zougen = ''
    else:
        if aLst[i] > aLst[i + 1]:
            zougen= 'D'
        elif aLst[i] < aLst[i + 1]:
            zougen = 'U'
print(cnt + 1)
