N, Q = map(int, input().split())
S = input()
mLst = [0] * N
for i in range(N - 1):
    if S[i: i + 2] == 'AC':
        mLst[i + 1] = mLst[i] + 1
    else:
        mLst[i + 1] = mLst[i]

lLst = [list(map(int, input().split())) for i in range(Q)]

for i in range(Q):
    print(mLst[lLst[i][1] - 1] - mLst[lLst[i][0] - 1])
