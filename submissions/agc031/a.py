from collections import defaultdict

INF = 10 ** 9 + 7
N = int(input())
S = input()

d = defaultdict(int)
for key in S:
    d[key] += 1

ans = 1
for i in d.items():
    ans *= (i[1] + 1)
    ans %= INF

print((ans - 1))
