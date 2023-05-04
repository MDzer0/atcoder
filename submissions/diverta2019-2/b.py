from collections import defaultdict

N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
xy.sort(key=lambda x: (x[0], x[1]))
dxy = defaultdict(int)
if N == 1:
    print(1)
    exit()

for i in range(N - 1):
    for j in range(i + 1, N):
        dxy[(xy[i][0] - xy[j][0], xy[i][1] - xy[j][1])] += 1

dxy = sorted(dxy.items(), key=lambda x: x[1], reverse=True)
print(N - dxy[0][1])
