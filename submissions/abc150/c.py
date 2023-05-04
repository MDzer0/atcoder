import itertools

N = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))
list = []
clst = [i for i in range(1, N + 1)]
for i in itertools.permutations(clst, N):
    list.append(i)

acnt = 0
bcnt = 0
for i in range(len(list)):
    aF = True
    for j in range(N):
        if list[i][j] != P[j]:
            aF = False
            break
    if aF:
        acnt = i + 1

for i in range(len(list)):
    bF = True
    for j in range(N):
        if list[i][j] != Q[j]:
            bF = False
            break
    if bF:
        bcnt = i + 1
print(abs(acnt - bcnt))
