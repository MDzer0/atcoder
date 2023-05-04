inData = str(input())
ansList = []
dataLen = len(inData)
zeroCnt = 0
oneCnt = 0
for i in range(0, dataLen):
    if inData[i] == '0':
        zeroCnt += 1
    else:
        oneCnt += 1

print(2 * min([zeroCnt, oneCnt]))
