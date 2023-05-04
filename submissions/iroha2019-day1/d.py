N, X, Y = map(int, input().split())
noraLst = list(map(int, input().split()))
XPow = X
YPow = Y
noraLst.sort(reverse=True)
for i in range(N):
    if i % 2 == 0:
        XPow += noraLst[i]
    else:
        YPow += noraLst[i]

if XPow > YPow:
    print('Takahashi')
elif XPow < YPow:
    print('Aoki')
else:
    print('Draw')
