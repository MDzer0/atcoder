H, W, X, Y = map(int, input().split())
S = [input() for _ in range(H)]

ans = 0
for i in range(X, H):
    if S[i][Y - 1] == '.':
        ans += 1
    else:
        break

for i in reversed(range(X)):
    if S[i][Y - 1] == '.':
        ans += 1
    else:
        break

for i in range(Y, W):
    if S[X - 1][i] == '.':
        ans += 1
    else:
        break

for i in reversed(range(max(0, Y - 1))):
    if S[X - 1][i] == '.':
        ans += 1
    else:
        break

print(ans)
