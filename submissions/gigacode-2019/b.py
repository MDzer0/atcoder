N, X, Y, Z = map(int, input().split())
cnt = 0
for i in range(N):
    a, b = map(int, input().split())
    if a >= X and b >= Y and a + b >= Z:
        cnt += 1

print(cnt)
