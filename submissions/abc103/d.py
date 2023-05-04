N, M = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(M)]
jogai = [0] * (N + 1)
ab.sort(key=lambda x: x[1])
cnt = 0
tmp = 0
for i in range(M):
    if tmp < ab[i][0]:
        tmp = ab[i][1] - 1
        cnt += 1

print(cnt)
