N = int(input())
ab = [list(map(int, input().split())) for _ in range(N)]
slist = []
for i in ab:
    slist.append(i[0])
    slist.append(i[1])

slist.sort()
ans = 10 ** 18
for i in range(2 * N):
    for j in range(2 * N):
        tmp = 0
        for k in range(N):
            tmp += abs(ab[k][0] - slist[i]) + abs(ab[k][1] - ab[k][0]) + abs(slist[j] - ab[k][1])
        ans = min(ans, tmp)

print(ans)
