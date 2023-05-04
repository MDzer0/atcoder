N, D = map(int, input().split())
cnt = 0
for i in range(N):
    x, y = map(int, input().split())
    if pow(pow(x, 2) + pow(y, 2), 0.5) <= D:
        cnt += 1

print(cnt)
