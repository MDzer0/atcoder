S = input()
K = int(input())

if len(S) == 1:
    print(K // 2)
    exit()

if len(S) == S.count(S[0]):
    print(len(S) * K // 2)
    exit()

cnt = 0
tmpCnt = 1
tmp = S[0]
tmpCntList = []
for i in range(1, len(S)):
    if tmp == S[i]:
        tmpCnt += 1
        tmp = S[i]
    else:
        tmpCntList.append(tmpCnt)
        cnt += tmpCnt // 2
        tmp = S[i]
        tmpCnt = 1

if tmpCnt != 1:
    cnt += tmpCnt // 2
    tmpCntList.append(tmpCnt)

ans = cnt * K
if S[0] == S[-1] and (tmpCnt % 2 != 0 and tmpCntList[0] % 2 != 0):
    print(ans + K - 1)
else:
    print(ans)
