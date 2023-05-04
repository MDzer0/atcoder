S = input()
jcnt = 0
icnt = 0
for i in range(len(S) - 2):
    if S[i] == 'J' and S[i + 1] == 'O' and S[i + 2] == 'I':
        jcnt += 1
    if S[i] == 'I' and S[i + 1] == 'O' and S[i + 2] == 'I':
        icnt += 1
print(jcnt)
print(icnt)
