N, M = map(int, input().split())
seito = [int(input()) for _ in range(N)]

for i in range(1, M + 1):
    for j in range(N - 1):
        if seito[j] % i > seito[j + 1] % i:
            tmp = seito[j]
            seito[j] = seito[j + 1]
            seito[j + 1] = tmp

for i in seito:
    print(i)
