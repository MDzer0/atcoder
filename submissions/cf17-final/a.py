import sys

S = input()
MOJI = 'AKIHABARA'
ans = 'YES'
if len(S) > 9:
    print('NO')
    sys.exit()

for i in range(9 - len(S)):
    S = S + 'A'
for i in range(9):
    if S[i] != MOJI[i]:
        if MOJI[i] != 'A':
            ans = 'NO'
            break
        else:
            S = S[0:i] + 'A' + S[i:]

print(ans)
