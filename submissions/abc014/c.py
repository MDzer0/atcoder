n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
rui = [0] * 1000005

for i in range(n):
    rui[ab[i][0]] = rui[ab[i][0]] + 1
    rui[ab[i][1] + 1] = rui[ab[i][1] + 1] - 1
for i in range(1000001):
    rui[i + 1] += rui[i]

print(max(rui))
