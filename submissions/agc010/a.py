N = int(input())
a = list(map(int, input().split()))
kcnt = 0
for i in range(N):
    if a[i] % 2 != 0:
        kcnt += 1

if kcnt % 2 == 0:
    print('YES')
else:
    print('NO')
