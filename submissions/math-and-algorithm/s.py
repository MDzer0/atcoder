N = int(input())
A = list(map(int, input().split()))

cntList = [0] * 3
for i in A:
    if i == 1: cntList[0] += 1
    elif i == 2: cntList[1] += 1
    else: cntList[2] += 1

ans = 0
for i in cntList:
    if i > 1:
        ans += ((i * (i - 1)) // 2)

print(ans)
