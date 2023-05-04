import bisect

N, M = map(int, input().split())
PY = [list(map(int, input().split())) for _ in range(M)]

sortY = [[] for _ in range(N)]
for i in range(M):
    sortY[PY[i][0] - 1].append(PY[i][1])

for i in range(N):
    sortY[i] = sorted(set(sortY[i]))

ansList = []
for i in range(M):
    indexY = bisect.bisect_left(sortY[PY[i][0] - 1], PY[i][1])
    print(str(PY[i][0]).zfill(6) + str(indexY + 1).zfill(6))
