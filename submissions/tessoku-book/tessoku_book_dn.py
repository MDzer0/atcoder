X, Y = map(int, input().split())
if X == 1 and Y == 1:
    print(0)
    exit()

ansList = []
tmpx = X
tmpy = Y
ansList.append((tmpx, tmpy))

while True:

    if tmpx > tmpy:
        tmpx -= tmpy
    else:
        tmpy -= tmpx
    if tmpx == 1 and tmpy == 1:
        break
    ansList.append((tmpx, tmpy))

print(len(ansList))
for i in reversed(ansList):
    print(*i)
