import itertools

N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]
combList = [_ for _ in range(1, N)]

ans = 0
for i in itertools.permutations(combList):
    tmp = T[0][i[0]]
    for j in range(len(i) - 1):
        tmp += T[i[j]][i[j + 1]]
    tmp += T[i[N - 2]][0]
    if tmp == K:
        ans += 1

print(ans)
