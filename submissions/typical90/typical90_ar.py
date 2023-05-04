N, Q = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
for i in range(Q):
    T, x, y = map(int, input().split())
    if T == 1:
        tmp = A[(x - 1 - cnt) % N]
        A[(x - 1 - cnt) % N] = A[(y - 1 - cnt) % N]
        A[(y - 1 - cnt) % N] = tmp
    elif T == 2:
        cnt += 1
    else:
        print(A[(x - 1 - cnt) % N])
