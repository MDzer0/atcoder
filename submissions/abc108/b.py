inLst = list(map(int, input().split()))

anslst = []
anslst.append(inLst[2] - (inLst[3] - inLst[1]))
anslst.append(inLst[3] + (inLst[2] - inLst[0]))
anslst.append(anslst[0] - (inLst[2] - inLst[0]))
anslst.append(anslst[1] - (inLst[3] - inLst[1]))

for i in anslst:
    print(i, end=' ')
