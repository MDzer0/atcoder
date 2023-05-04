N, M = map(int, input().split())
KA = [list(map(int, input().split())) for _ in range(N)]
P, Q = map(int, input().split())
B = list(map(int, input().split()))

ans = 0
for i in range(N):
    cnt = 0
    for j in KA[i][1:]:
        for k in B:
            if j == k:
                cnt += 1
    if cnt >= Q:
        ans += 1

print(ans)
