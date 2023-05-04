D = int(input())
A = [int(input()) for _ in range(D)]
Q = int(input())
kabuka = [0] * D
kabuka[0] = A[0]
for i in range(1, D):
    kabuka[i] = kabuka[i - 1] + A[i]

for i in range(Q):
    S, T = map(int, input().split())
    if kabuka[S - 1] > kabuka[T - 1]:
        print(S)
    elif kabuka[S - 1] < kabuka[T - 1]:
        print(T)
    else:
        print('Same')
