N = int(input())
a = [int(input()) for _ in range(N)]
tmp = a[0]
for i in range(1, N):
    if tmp == a[i]:
        print('stay')
    elif tmp > a[i]:
        print('down', tmp - a[i])
    else:
        print('up', a[i] - tmp)

    tmp = a[i]
