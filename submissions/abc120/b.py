inData = input().split(' ')

seisu1 = int(inData[0])
seisu2 = int(inData[1])
ansK = int(inData[2])
ansList = []
maxSeisu = min([seisu1, seisu2])

for i in range(1, maxSeisu + 1):
    if (seisu1 % i == 0) and (seisu2 % i == 0):
        ansList.append(i)

ansListLen = len(ansList)
print(ansList[ansListLen - ansK])
