S = input()
if int(S[2:]) >= 1 and int(S[2:]) <= 12:
    if int(S[:2]) <= 12 and int(S[:2]) >= 1:
        print('AMBIGUOUS')
    else:
        print('YYMM')
elif int(S[2:]) >= 13:
    if int(S[:2]) >= 1 and int(S[:2]) <= 12:
        print('MMYY')
    else:
        print('NA')
else:
    if int(S[2:]) == 0:
        if int(S[:2]) >= 1 and int(S[:2]) <= 12:
            print('MMYY')
        else:
            print('NA')
    else:
        print('NA')

