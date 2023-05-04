import itertools

N, M, L = map(int, input().split())
P, Q, R = map(int, input().split())

ans = 0

for x, y, z in itertools.permutations([P, Q, R], 3):
    ans = max(ans, (N // x) * (M // y) * (L // z))

print(ans)
