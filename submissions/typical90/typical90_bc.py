import itertools

N, P, Q = map(int, input().split())
A = list(map(int, input().split()))
ans = 0

for a, b, c, d, e in itertools.combinations(A, 5):
    tmp = a * b % P * c % P * d % P * e % P
    if tmp == Q:
        ans += 1

print(ans)
