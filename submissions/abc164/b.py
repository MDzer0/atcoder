A, B, C, D = map(int, input().split())
cnt = 0
while True:
    if cnt % 2 == 0:
        C -= B
        cnt += 1
        if C <= 0:
            print('Yes')
            break
    else:
        A -= D
        cnt += 1
        if A <= 0:
            print('No')
            break
