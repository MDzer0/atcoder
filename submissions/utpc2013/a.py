one_list = set(['A', 'D', 'O', 'P', 'Q', 'R'])

S = input()
cnt = 0
for i in range(4):
    if i != 2:
        if S[i] in one_list or S[i] == 'B':
            print('no')
            exit()
    else:
        if not S[i] in one_list:
            print('no')
            exit()

print('yes')
