N, K = map(int, input().split())
v = list(map(int, input().split()))
ans = 0

for i in range(min(K + 1, N + 1)):
    for j in range(min(K + 1 - i, N + 1 - i)):
        d = K - i -j
        nowlst = v[:i] + v[N - j:]
        nowlst.sort(reverse=True)
        for k in range(d):
            if nowlst != [] and nowlst[-1] < 0:
                nowlst.pop()
            else:
                break
        ans = max(ans, sum(nowlst))

print(ans)
