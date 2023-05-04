N = int(input())
ab = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    total = ab[i][0] + ab[i][1]
    ab[i].append(total)
ab.sort(key=lambda x: x[2], reverse=True)
ans = 0
for i in range(N):
    if i % 2 == 0:
        ans += ab[i][0]
    else:
        ans -= ab[i][1]

print(ans)
