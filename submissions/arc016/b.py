N = int(input())
x = [list(input()) for _ in range(N)]
cnt = 0
for i in range(N):
    for j in range(len(x[i])):
        if x[i][j] == 'x':
            cnt += 1


for i in range(9):
    tmp = ''
    for j in range(N):
        if tmp != 'o' and x[j][i] == 'o':
            tmp = x[j][i]
            cnt += 1
            continue
        if x[j][i] != 'o':
            tmp = x[j][i]
            continue

print(cnt)
