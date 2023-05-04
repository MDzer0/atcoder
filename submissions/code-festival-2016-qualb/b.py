N, A, B = map(int, input().split())
S = input()
cnt = 0
cntb = 1
for i in S:
    if i == 'a':
       if cnt < A + B:
           cnt += 1
           print('Yes')
       else:
           print('No')
    elif i == 'b':
        if cnt < A + B and cntb <= B:
            cnt += 1
            cntb += 1
            print('Yes')
        else:
            print('No')
    else:
        print('No')
