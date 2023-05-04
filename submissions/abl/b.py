A, B, C, D = map(int, input().split())

if A <= C:
    if A <= C <= B:
        print('Yes')
    else:
        print('No')
else:
    if C <= A <= D:
        print('Yes')
    else:
        print('No')
