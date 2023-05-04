N, L = map(int, input().split())
sList = []

for i in range(N):
    sList.append(input())

sList.sort()

for i in sList:
    print(i, end='')
