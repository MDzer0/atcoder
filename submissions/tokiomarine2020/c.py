import copy

N, K = map(int, input().split())
a = list(map(int, input().split()))

ans = [0] * N
def loop():
    global a
    ruir = [0] * (N + 1)
    ruil = [0] * (N + 1)
    for i in range(N):
        ruir[i] += 1
        tmp = i + a[i]
        if tmp < N:
           ruir[tmp + 1] -= 1
    for i in range(N):
        ruir[i + 1] += ruir[i]

    for i in reversed(range(N)):
        if a[i] - 0.5 > -1:
            ruil[i - 1] += 1
            tmp = i - a[i]
            if tmp > 0:
                ruil[tmp - 1] -= 1
    for i in reversed(range(N)):
        ruil[i - 1] += ruil[i]
    cnt = 0
    for i in range(N):
        add = ruir[i] + ruil[i]
        if add > N:
            add = N
        if add == N:
            cnt +=1
        ans[i] = add
    if cnt == N:
        print(*ans)
        exit()
    a = copy.deepcopy(ans)

for i in range(K):
    loop()
print(*ans)
