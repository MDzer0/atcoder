abc = list(map(int, input().split()))
K = int(input())
tmp = [i for i in range(K)]
ans = 'No'

for i in range(K + 1):
    for j in range(K + 1):
        for k in range(K + 1):
            if i + j + k == K:
                tmpabc = []
                tmplst = [i, j, k]
                for l in range(3):
                    tmpabc.append(abc[l] * (2 ** tmplst[l]))
                if tmpabc[0] < tmpabc[1] and tmpabc[1] < tmpabc[2]:
                    ans = 'Yes'
                    break

print(ans)
