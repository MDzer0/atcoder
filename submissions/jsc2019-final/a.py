N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
w = [0] * (max(A) + max(B) + 1)
for i in range(N):
    for j in range(M):
        tmp = A[i] + B[j]
        if w[tmp] == 0:
            w[tmp] = (i, j)
        else:
            a, b = w[tmp]
            print(a, b, i, j)
            exit()

print(-1)
