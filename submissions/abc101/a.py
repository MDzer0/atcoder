S = input()
ansCnt = 0
for i in S:
    if i == '+':
        ansCnt += 1
    else:
        ansCnt -= 1
print(ansCnt)
