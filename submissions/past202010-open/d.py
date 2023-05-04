N = int(input())
S = list(input())
cnt = 10 ** 10
l, r = 10 ** 10, 10 ** 10
for i in range(N + 1):
    tmpS = S[:]
    for j in range(N - i):
        for k in range(1, N):
            if tmpS[k] == '#':
                tmpS[k - 1] = '#'
    if tmpS.count('.') == 0:
        if cnt > N - i:
            cnt = N - i
            l = N - i
            r = 0
            continue
    for j in range(N - 1):
        for k in range(N - 2, -1, -1):
            if tmpS[k] == '#':
                tmpS[k + 1] = '#'
        if tmpS.count('.') == 0:
            if cnt > N - i + j + 1:
                cnt = N - i + j + 1
                l = N - i
                r = j + 1
                break

print(l, r)
