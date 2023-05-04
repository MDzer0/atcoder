H, W = map(int, input().split())
S = [input() for _ in range(H)]
ans = 0
for i in S:
    for j in i:
        if j == '#':
            ans += 1
print(ans)
