N = int(input())
s = [list(input()) for _ in range(N)]
rcnt = 0
bcnt = 0
for i in range(N):
    for j in range(N):
        if s[i][j] == 'R':
            rcnt += 1
        elif s[i][j] == 'B':
            bcnt += 1

if rcnt > bcnt:
    print('TAKAHASHI')
elif rcnt < bcnt:
    print('AOKI')
else:
    print('DRAW')
