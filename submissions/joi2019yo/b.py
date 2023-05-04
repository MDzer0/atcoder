N = int(input())
X = list(map(int, input().split()))
M = int(input())
A = list(map(int, input().split()))

for i in range(M):
    if A[i] != N:
        if X[A[i] - 1] + 1 != X[A[i]] and X[A[i] - 1] != 2019:
            X[A[i] - 1] += 1
    elif X[A[i] - 1] != 2019:
        X[A[i] - 1] += 1

for i in X:
    print(i)
