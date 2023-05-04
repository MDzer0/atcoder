N, M = map(int, input().split())
H = list(map(int, input().split()))
d = [[] for _ in range(N)]

for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    d[b].append(a)
    d[a].append(b)

ans = 0
cnt = 0
for i in d:
    if i != []:
        cntF = True
        for j in i:
            if H[cnt] <= H[j]:
                cntF = False
                break
        if cntF:
            ans += 1
    else:
        ans += 1
    cnt += 1

print(ans)
