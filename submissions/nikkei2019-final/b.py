N, M, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

if M > N:
    print('X')
elif N > M:
    print('Y')
else:
    for i in range(N):
        if a[i] > b[i]:
            print('Y')
            exit()
        elif a[i] < b[i]:
            print('X')
            exit()
    print('Same')
