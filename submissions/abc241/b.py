from collections import defaultdict

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dictA = defaultdict(int)
dictB = defaultdict(int)

for i in A:
    dictA[i] += 1

for i in B:
    dictB[i] += 1

for v, m in dictB.items():
    if m > dictA[v]:
        print('No')
        exit()

print('Yes')
