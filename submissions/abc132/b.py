n = input()
plst = list(map(int, input().split()))

anscnt = 0
for i in range(1, len(plst) - 1):
    if plst[i - 1] < plst[i] and plst[i] < plst[i + 1]:
        anscnt += 1
    elif plst[i + 1] < plst[i] and plst[i] < plst[i - 1]:
        anscnt += 1

print(anscnt)
