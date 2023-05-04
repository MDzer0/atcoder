N = int(input())
iLst = []
jLst = []
ans = 2025 - N
for i in range(1, 10):
    for j in range(1, 10):
        tmp = i * j
        if ans == tmp:
            iLst.append(i)
            jLst.append(j)

for i in range(len(iLst)):
    print(str(iLst[i]) + ' x ' + str(jLst[i]))
