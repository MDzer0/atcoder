N = int(input())
D, X = map(int, input().split())

eCnt = X
for i in range(N):
    tmp = int(input())
    eCnt += 1
    for i in range(tmp + 1, D + 1, tmp):
        eCnt += 1

print(eCnt)
