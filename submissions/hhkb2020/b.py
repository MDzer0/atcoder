H, W = map(int, input().split())
s = [input() for _ in range(H)]
ans = 0
for i in range(H):
    cnt = 0
    for j in range(W):
        if s[i][j] == '.':
            cnt += 1
        else:
            if cnt != 0:
                ans += cnt - 1
                cnt = 0
    if cnt != 0:
        ans += cnt - 1

for i in range(W):
    cnt = 0
    for j in range(H):
        if s[j][i] == '.':
            cnt += 1
        else:
            if cnt != 0:
                ans += cnt - 1
                cnt = 0
    if cnt != 0:
        ans += cnt - 1

print(ans)
