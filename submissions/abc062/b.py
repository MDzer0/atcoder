H, W = map(int, input().split())
ansLst = []
ansLst.append('#' * (W + 2))
for i in range(H):
    ansLst.append('#' + input() + '#')
ansLst.append('#' * (W + 2))
for i in ansLst:
    print(i)
