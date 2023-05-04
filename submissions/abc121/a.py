inData1 = input().split(' ')
inData2 = input().split(' ')
sMasu = int(inData1[0]) * int(inData1[1])

sMasu -= int(inData1[1]) * int(inData2[0])
sMasu -= (int(inData1[0]) - int(inData2[0])) * int(inData2[1])

print(sMasu)
