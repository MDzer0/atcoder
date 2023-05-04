N = int(input())
A = list(map(int, input().split()))

Left = [0] * (N + 1)
Right = [0] * (N + 1)

for i in range(N):
    Left[i + 1] = max(Left[i], A[i])
    Right[-i - 2] = max(Right[-i - 1], A[-i - 1])

D = int(input())
for i in range(D):
    l, r = map(int, input().split())
    print(max(Left[l - 1], Right[r]))
