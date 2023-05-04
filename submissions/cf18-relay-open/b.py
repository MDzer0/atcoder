import itertools

S = input()
x, y = map(int, input().split())
sousa = ['L', 'R', 'U', 'D']
slist = ['W', 'X', 'Y', 'Z']
sindex = [0, 1, 2, 3]

if x == 0 and y == 0:
    print('Yes')
    exit()

for i in itertools.permutations(sindex):
    tmpx, tmpy = 0, 0
    tmp = []
    for j in range(4):
        tmp.append(slist[i[j]])

    for j in S:
        t = sousa[tmp.index(j)]
        if t == 'L':
            tmpx -= 1
        elif t == 'R':
            tmpx += 1
        elif t == 'U':
            tmpy += 1
        else:
            tmpy -= 1
        if x == tmpx and y == tmpy:
            print('Yes')
            exit()

print('No')
