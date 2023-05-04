A = list(map(int, input().split()))
cntList = [0] * 13

for i in A:
    cntList[i - 1] += 1

cntList.sort(reverse=True)
if cntList[0] == 3 and cntList[1] == 2:
    print('Yes')
else:
    print('No')
