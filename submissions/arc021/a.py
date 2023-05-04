a = [list(map(int, input().split())) for _ in range(4)]
ans = 'GAMEOVER'
for i in range(4):
    for j in range(3):
        if a[i][j] == a[i][j + 1]:
            ans = 'CONTINUE'
            break
if ans == 'CONTINUE':
    print(ans)
else:
    for i in range(4):
        for j in range(3):
            if a[j][i] == a[j + 1][i]:
                ans = 'CONTINUE'
                break
    print(ans)
