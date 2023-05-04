N = int(input())
aLst = list(map(int, input().split()))
tmp = 0
for i in range(N):
    tmp = tmp ^ aLst[i]

if tmp == 0:
    print('Yes')
else:
    print('No')
