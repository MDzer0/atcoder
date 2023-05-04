N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())
kokan = [_ for _ in range(N + 1)]
for i in range(Q):
    ope = list(map(int, input().split()))
    if ope[0] == 1:
        tmp = kokan[ope[1]]
        kokan[ope[1]] = kokan[ope[2]]
        kokan[ope[2]] = tmp
    else:
        print(A[kokan[ope[1]] - 1][ope[2] - 1])
