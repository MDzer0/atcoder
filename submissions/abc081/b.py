import math

N = int(input())
A = list(map(int, input().split()))
ans = 0
ans = math.gcd(0, A[0])

for i in A:
    ans = math.gcd(ans, i)

for i in range(40):
    if pow(2, i) == ans:
        print(i)
        exit()
