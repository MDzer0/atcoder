from collections import defaultdict
MOD = 10 ** 9 + 7

N = int(input())
T = [int(input()) for _ in range(N)]
d = defaultdict(int)
T.sort()
total = 0
ans1 = 0
for i in T:
    ans1 += total + i
    total += i
    d[i] += 1
print(ans1)

ans2 = 1
for i, j in d.items():
    for k in range(1, j + 1):
        ans2 *= k
        ans2 %= MOD

print(ans2)
