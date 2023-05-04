L, H = map(int, input().split())
N = int(input())
aLst = list(int(input()) for i in range(N))
ansLst = [0] * N
for i in range(N):
    if L > aLst[i]:
        ansLst[i] = L - aLst[i]
    elif H < aLst[i]:
        ansLst[i] = -1

for i in ansLst:
    print(i)
