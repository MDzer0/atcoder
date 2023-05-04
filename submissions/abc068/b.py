N = int(input())
ans = 0
maxCnt = 0

for i in range(1, N + 1):
    tmpCnt = 0
    tmp = i
    if i % 2 == 0:
        for j in range(i):
            tmp = tmp // 2
            tmpCnt += 1
            if tmp % 2 != 0:
                break
    if maxCnt <= tmpCnt:
        maxCnt = tmpCnt
        ans = i

print(ans)
