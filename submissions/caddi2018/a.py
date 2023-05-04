from collections import defaultdict
sosu = defaultdict(int)
def soinsu(n):
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            n //= i
            sosu[i] += 1
    if n > 1:
        sosu[n] += 1
    return

N, P = map(int, input().split())
soinsu(P)
ans = 1
for i, j in sosu.items():
    ans *= i ** (j // N)

print(ans)
