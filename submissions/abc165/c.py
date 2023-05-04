import itertools

N, M, Q = map(int, input().split())
abcd = [list(map(int, input().split())) for _ in range(Q)]
ans = 0

for i in itertools.combinations_with_replacement(range(1, M + 1), N):
    total = 0
    for j in range(Q):
        if i[abcd[j][1] - 1] - i[abcd[j][0] - 1] == abcd[j][2]:
            total += abcd[j][3]
    ans = max(ans, total)

print(ans)
