N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
aMax = 0
bMin = 10 ** 10

for i in range(N):
    aMax = max(aMax, A[i])
    bMin = min(bMin, B[i])


print(max(0, bMin - aMax + 1))
