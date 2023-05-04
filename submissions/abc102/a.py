N = int(input())

for i in range(N, 2*N + 1, N):
    if i % N == 0 and i % 2 == 0:
        print(i)
        break
