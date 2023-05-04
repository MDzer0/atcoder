import bisect
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

AB = []
CD = []

for i in range(N):
    for j in range(N):
        AB.append(A[i] + B[j])
        CD.append(C[i] + D[j])

AB.sort()

for i in range(N ** 2):
    tmp = bisect.bisect_left(AB, K - CD[i])
    if tmp < N ** 2 and AB[tmp] == K - CD[i]:
        print('Yes')
        exit()
print('No')
