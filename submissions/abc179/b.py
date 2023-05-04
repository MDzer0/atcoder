N = int(input())
cnt = 0
maxcnt = 0
for i in range(N):
    d1, d2 = map(int, input().split())
    if d1 == d2:
        cnt += 1
        maxcnt = max(maxcnt, cnt)
    else:
        cnt = 0

if maxcnt >= 3:
    print('Yes')
else:
    print('No')
