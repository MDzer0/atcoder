N = int(input())
xl = [list(map(int, input().split())) for _ in range(N)]
rl = []
for i in range(N):
    rl.append((xl[i][0] - xl[i][1], xl[i][0] + xl[i][1]))
rl.sort(key=lambda x: x[1])
cnt = 0
tmp = -10 ** 18

for i, j in rl:
    if tmp <= i:
        cnt += 1
        tmp = j
print(cnt)
