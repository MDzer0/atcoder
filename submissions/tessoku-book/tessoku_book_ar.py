N, Q = map(int, input().split())
A = [_ for _ in range(1, N + 1)]
reversCnt = 0

for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        if reversCnt % 2 == 0:
            A[query[1] - 1] = query[2]
        else:
            A[-query[1]] = query[2]
    elif query[0] == 2:
        reversCnt += 1
    else:
        if reversCnt % 2 == 0:
            print(A[query[1] - 1])
        else:
            print(A[-query[1]])
