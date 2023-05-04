import string
H, W = map(int, input().split())
hw = [list(input().split()) for _ in range(H)]
ans = []
sans = ''
for i in range(H):
    for j in range(W):
        if hw[i][j] == 'snuke':
            ans.append(i)
            ans.append(j)
            break

sans = string.ascii_uppercase[ans[1]] + str(ans[0] + 1)

print(sans)
