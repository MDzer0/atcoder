a, b = map(int, input().split())
if a >= 8:
    print('No')
else:
    if b == a * 2 or b == a * 2 + 1:
        print('Yes')
    else:
        print('No')
