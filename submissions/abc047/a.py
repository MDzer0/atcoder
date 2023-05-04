klist = list(map(int, input().split()))
klist.sort()

if klist[2] == klist[0] + klist[1]:
    print('Yes')
else:
    print('No')
