N = int(input())
vLst = list(map(int, input().split()))
cLst = list(map(int, input().split()))

total = 0
for i in range(N):
    if vLst[i] > cLst[i]:
        total += vLst[i] - cLst[i]
print(total)
