N = int(input())
S = list(input() for _ in range(N))
comp = 'indeednow'

for i in range(N):
    compF = True
    for j in comp:
        if comp.count(j) != S[i].count(j):
            compF = False
            break
    if compF:
        print('YES')
    else:
        print('NO')
