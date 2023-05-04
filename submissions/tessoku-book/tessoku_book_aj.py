N, K = map(int, input().split())
if 2 * N - 2 <= K and K % 2 == 0:
    print('Yes')
else:
    print('No')
