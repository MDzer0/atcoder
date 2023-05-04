inList = []
for i in range(5):
    inList.append(int(input()))
k = int(input())
kList = []
for i in range(5):
    for j in range(1, 5):
        kyori = int(abs(inList[i] - inList[j]))
        kList.append(kyori)
ansFlg = True
for i in kList:
    if k < i:
        ansFlg = False
if ansFlg:
    print('Yay!')
else:
    print(':(')
