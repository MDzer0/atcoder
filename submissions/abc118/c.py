from fractions import gcd
N = int(input())
alst = list(map(int, input().split()))
ans = alst[0]
for i in range(1, N):
    if ans > alst[i]:
        ans = gcd(ans, alst[i])
    else:
        ans = gcd(alst[i], ans)
print(ans)
