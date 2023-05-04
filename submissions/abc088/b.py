N = int(input())
kList = list(map(int, input().split()))
aTotal = 0
bTotal = 0
kList.sort(reverse=True)

for i in range(N):
    if i % 2 == 0:
        aTotal += kList[i]
    else:
        bTotal += kList[i]

print(aTotal - bTotal)
