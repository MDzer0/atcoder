inData = input().split(' ')
N = int(inData[0])
M = int(inData[1])
ZERO = 0
seisuC = int(inData[2])
seisuB = input().split(' ')
ansCnt = 0
for i in range(0, N):
    inData2 = input().split(' ')
    calc = 0
    for j in range(0, len(inData2)):
        calc += (int(inData2[j]) * int(seisuB[j]))
    calc += seisuC
    if calc > ZERO:
        ansCnt += 1

print(ansCnt)
