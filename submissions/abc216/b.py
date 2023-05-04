N = int(input())
ST = [input() for _ in range(N)]

for i in range(N - 1):
    for j in range(i + 1, N):
        if ST[i] == ST[j]:
            print('Yes')
            exit()

print('No')
