ANS = 'CODEFESTIVAL2016'
S = input()
cnt = 0
for i in range(len(S)):
    if S[i] != ANS[i]:
        cnt += 1

print(cnt)
