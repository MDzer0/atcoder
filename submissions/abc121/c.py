N, M = map(int, input().split())
mseList = [list(map(int, input().split())) for i in range(0, N)]
mseList = sorted(mseList, key=lambda x:x[0])
total = 0
for i, k in mseList:
    if k < M:
        total += i * k
        M -= k
    else:
        total += i * M
        break
print(total)
