N, K = map(int, input().split())
ab = []

for i in range(N):
    a, b = map(int, input().split())
    ab.append(b)
    ab.append(a - b)

ab.sort(reverse=True)
print(sum(ab[:K]))
