r, D, x = map(int, input().split())
ansLst = [0] * 10

ansLst[0] = int((r * x) - D)
for i in range(1, 10):
    ansLst[i] = int((ansLst[i - 1] * r) - D)
for i in ansLst:
    print(i)
