N, M = map(int, input().split())
start = 0
if N == 1:
    start = 0
elif N == 2:
    start = 10
else:
    start = 100
N = str(N)

sc = [list(input().split()) for _ in range(M)]

for i in range(start, 1000):
    ansF = True
    for j in range(M):
        if str(i)[int(sc[j][0]) - 1] != sc[j][1]:
            ansF = False
            break
    if ansF:
        print(i)
        exit()

print(-1)
