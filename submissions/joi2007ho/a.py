n, m = map(int, input().split())
a = list(int(input()) for _ in range(n))
maxA = -10 ** 18

rui = [0] * (n + 1)
for i in range(1, n + 1):
    rui[i] += rui[i - 1] + a[i - 1]

for i in range(m, n + 1):
    maxA = max(maxA, rui[i] - rui[i - m])

print(maxA)
