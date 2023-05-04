s = input()

sLst = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',\
        'o','p','q','l','s','t','u','v','w','x', 'y', 'z']
ansLst = []

for i in sLst:
    if s.count(i) == 0:
        ansLst.append(i)

if len(ansLst) == 0:
    print('None')
else:
    ansLst.sort()
    print(ansLst[0])
