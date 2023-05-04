import fractions
N, M = map(int, input().split())
S = input()
T = input()
ans = (N * M) // fractions.gcd(N, M)
n = N // fractions.gcd(N, M)
m = M // fractions.gcd(N, M)
for i in range(min(N // n, M // m)):
    tmpn = S[n * i]
    tmpm = T[m * i]
    if tmpn != tmpm:
        ans = -1
        break

print(ans)
