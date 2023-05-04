from collections import defaultdict
import math

INF = 10 ** 6 + 1
is_prime = [1] * INF

def eratorasu():
    is_prime[0] = 0
    is_prime[1] = 0
    for i in range(2, INF):
        if is_prime[i] == 0:
            continue
        for j in range(i * 2, INF, i):
            is_prime[j] = 0
    return

def f(n):
    yakusu = []
    if is_prime[n]:
        yakusu.append(n)
    else:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                yakusu.append(i)
                if i != n //i:
                    yakusu.append(n // i)
                break

    for i in yakusu:
        if i != 1:
            d[i] += 1

eratorasu()
d = defaultdict(int)
N = int(input())
A = list(map(int, input().split()))

tmp = A[0]
for i in range(1, N):
    tmp = math.gcd(tmp, A[i])
    f(A[i])

if tmp != 1:
    print('not coprime')
    exit()
eratorasu()
f(A[0])

for i, v in d.items():
    if v != 1:
        print('setwise coprime')
        exit()

print('pairwise coprime')
