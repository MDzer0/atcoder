N, A, B = map(int, input().split())

for i in range(N):
    if i % 2 == 0:
        if N >= A:
            N -= A
        else:
            N = 0

        if N == 0:
            print('Ant')
            break
    else:
        if N >= B:
            N -= B
        else:
            N = 0

        if N == 0:
            print('Bug')
            break
