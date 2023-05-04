import sys
S = input()
for i in range(len(S)):
    if S.count(S[i]) >= 2:
        print('no')
        sys.exit()

print('yes')
