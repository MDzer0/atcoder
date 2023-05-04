S = input()

editS = S[2:-1:]

if S[0] == 'A' and S[1].islower and editS.count('C') == 1\
    and S[-1].islower():
    S = S.replace('A', '')
    S = S.replace('C', '')
    if S.islower():
        print('AC')
    else:
        print('WA')
else:
    print('WA')
