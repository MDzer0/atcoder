N, C, K = map(int, input().split())
t = list(int(input()) for _ in range(N))
t.sort()
ans = 0
s = t[0] + K
cnt = 0
cntF = True
for i in range(N):
    cntF = True
    if t[i] <= s:
        if cnt == C:
            cnt = 1
            ans += 1
            s = t[i] + K
            cntF = False
        else:
            cnt += 1
        continue

    cnt = 1
    s = t[i] + K
    ans += 1
if cntF:
    ans += 1

print(ans)
