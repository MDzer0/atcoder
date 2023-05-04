a = [list(map(int, input().split())) for _ in range(3)]
N = int(input())
b = [int(input()) for i in range(N)]
for k in range(N):
    for i in range(3):
        for j in range(3):
            if a[i][j] == b[k]:
                a[i][j] = 0

ans = 'Yes'
for i in range(3):
    cnt = 0
    for j in range(3):
        if a[i][j] != 0:
            break
        else:
            cnt += 1
    if cnt == 3:
        break
        
if cnt == 3:
    print(ans)
    exit()

for i in range(3):
    cnt = 0
    for j in range(3):
        if a[j][i] != 0:
            break
        else:
            cnt += 1
    if cnt == 3:
        break

if cnt == 3:
    print(ans)
    exit()

if a[0][0] == 0 and a[1][1] == 0 and a[2][2] == 0:
    print('Yes')
    exit()

if a[0][2] == 0 and a[1][1] == 0 and a[2][0] == 0:
    print('Yes')
else:
    print('No')
