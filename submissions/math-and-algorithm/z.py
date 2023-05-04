N, M = map(int, input().split())
ki = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    ki[a - 1].append(b - 1)
    ki[b - 1].append(a - 1)

ans = 0
for i in range(N):
    cnt = 0
    for j in ki[i]:
        if i > j:
            cnt += 1
    if cnt == 1:
        ans += 1

print(ans)
