s = input()
cnt = 1
tmp = s[0]
cntLst = []
for i in range(1, len(s)):
    if s[i - 1] == s[i]:
        cnt += 1
    else:
        tmp = s[i]
        cntLst.append(cnt)
        cnt = 1
cntLst.append(cnt)
ansLst = []
index = 0
for i in range(len(cntLst)):
    ansLst.append(s[index])
    ansLst.append(cntLst[i])
    index += cntLst[i]

for i in ansLst:
    print(i, end='')
print()
