N, X = map(int, input().split())
X *= 100
total = 0
for i in range(N):
    V, P = map(int, input().split())
    total += V * P
    if X < total:
        print(i + 1)
        exit()

print(-1)
