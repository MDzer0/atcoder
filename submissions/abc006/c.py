import sys

N, M = map(int, input().split())

if N * 2 > M or N * 4 < M:
    print(-1, -1, -1)
    sys.exit()

for i in range(2):
    tmp = i * 3
    for j in range((N + 1) - i):
        if M - tmp == (2 * j) + (4 * (N - i - j)):
            print(j, i, (N - i - j))
            sys.exit()

print(-1, -1, -1)
