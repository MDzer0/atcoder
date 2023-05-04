A, B = map(int, input().split())

mint = min(A, B)
tmp = abs(A - B)
if mint == 0:
    print('IMPOSSIBLE')
else:
    ans = tmp // 2
    tmp = tmp % 2
    if tmp == 0:
        print(ans + mint)
    else:
        print('IMPOSSIBLE')
