N = int(input())
ansList = []

for i in range(1 << N):
    left = 0
    right = 0
    tmp = ''
    ansF = True
    for j in range(N):
        if left < right:
            ansF = False
            break

        if i >> j & 1:
            tmp += '('
            left += 1
        else:
            tmp += ')'
            right += 1

    if ansF and left == right:
        ansList.append(tmp)

ansList.sort()
for i in ansList:
    print(i)
