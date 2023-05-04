abc = list(map(int, input().split()))
cnt1 = abc.count(abc[0])
cnt2 = abc.count(abc[1])
cnt3 = abc.count(abc[2])

if cnt1 == 2 or cnt2 == 2 or cnt3 == 2:
    print('Yes')
else:
    print('No')
