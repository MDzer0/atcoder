N = int(input())
nijigen = [[0] * (1502) for _ in range(1502)]

for i in range(N):
    A, B, C, D = map(int, input().split())
    nijigen[A][B] += 1
    nijigen[A][D] -= 1
    nijigen[C][B] -= 1
    nijigen[C][D] += 1

for i in range(1501):
    for j in range(1501):
        nijigen[i][j + 1] += nijigen[i][j]

for i in range(1501):
    for j in range(1501):
        nijigen[j + 1][i] += nijigen[j][i]

ans = 0
for i in range(1502):
    for j in range(1502):
        if nijigen[i][j] >= 1:
            ans += 1
print(ans)
