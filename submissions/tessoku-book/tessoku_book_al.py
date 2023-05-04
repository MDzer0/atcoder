D, N = map(int, input().split())
jikan = [24] * D

for i in range(N):
    l, r, h = map(int, input().split())
    for j in range(l, r + 1):
        jikan[j - 1] = min(jikan[j - 1], h)
print(sum(jikan))
