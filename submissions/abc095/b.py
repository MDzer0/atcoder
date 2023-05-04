N, X = map(int, input().split())
m = [int(input()) for _ in range(N)]
summ = sum(m)
minm = min(m)
X -= summ
print(N + (X // minm))
