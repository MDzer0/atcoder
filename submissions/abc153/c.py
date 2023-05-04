N, K = map(int, input().split())
h = list(map(int, input().split()))
h.sort(reverse=True)

ans = sum(h[K:])
print(ans)
