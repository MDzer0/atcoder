N = int(input())
T = [list('.' + input() + '.') for _ in range(N)]
insert = ['.'] * (2 * N + 1)
T.insert(0, insert)
T.append(insert)

for i in range(N, 0, -1):
    for j in range(1, 2 * N):
        if T[i][j] == '#':
            if T[i + 1][j - 1] == 'X' or T[i + 1][j] == 'X' or T[i + 1][j + 1] == 'X':
                T[i][j] = 'X'

for i in range(1, N + 1):
    print(''.join(T[i][1:2*N]))
