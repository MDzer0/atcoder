N = int(input())
A = list(map(int, input().split()))
sortA = []
for i in range(N):
    sortA.append((A[i], i + 1))
sortA.sort()

print(sortA[N - 2][1])
