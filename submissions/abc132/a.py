S = input()

cnt1 = S.count(S[0])
cnt2 = S.count(S[1])
cnt3 = S.count(S[2])
cnt4 = S.count(S[3])

if cnt1 == 2 and cnt2 == 2 and cnt3 == 2 and cnt4 == 2:
    print('Yes')
else:
    print('No')
