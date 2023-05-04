import sys
input = sys.stdin.readline
import math

def combnations(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

INF = 10 ** 9 + 7
N, K = map(int, input().split())
for i in range(1, K + 1):
    if N - K + 1 < i:
        print(0)
        continue
    ans = combnations(N - K + 1, i) * combnations(K - 1, i - 1)
    ans %= INF
    print(ans)
