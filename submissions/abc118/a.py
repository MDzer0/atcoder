inputData = input().split(' ')
ans = 0

if int(inputData[1]) % int(inputData[0]) ==0:
    ans = int(inputData[0]) + int(inputData[1])
else:
    ans = int(inputData[1]) - int(inputData[0])
print(ans)
