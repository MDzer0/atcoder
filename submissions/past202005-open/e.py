N, M, Q = map(int, input().split())
d = [[] for _ in range(N)]

for i in range(M):
    u, v = map(int, input().split())
    d[u - 1].append(v - 1)
    d[v - 1].append(u - 1)

C = list(map(int, input().split()))

for i in range(Q):
    s = list(input().split())
    print(C[int(s[1]) - 1])
    if s[0] == '2':
        C[int(s[1]) - 1] = int(s[2])
    else:
        for j in d[int(s[1]) - 1]:
            C[int(j)] = C[int(s[1]) - 1]
