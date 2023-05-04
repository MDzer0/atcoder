N, X = map(int, input().split())

for i in range(2, 11):
    tmp = ''
    tmpN = N
    while True:
        m, d =divmod(tmpN, i)
        tmp += str(d)
        tmpN = m
        if tmpN < i:
            tmp += str(tmpN)
            break
    if X == int(tmp[::-1]):
        print(i)
        exit()
