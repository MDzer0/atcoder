N, L = map(int, input().split())
amida = [list(input()) for _ in range(L + 1)]

for i in range(0, 2 * N, 2):
    tmp = i
    for j in range(L + 1):
        if tmp > 0 and amida[j][tmp - 1] == '-':
            tmp -= 2
        elif tmp < 2 * (N - 1) and amida[j][tmp + 1] == '-':
            tmp += 2
        elif j == L and amida[j][tmp] == 'o':
            print((i // 2) + 1)
            exit()


