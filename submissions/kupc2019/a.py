N, X = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
amax = max(a)
cnt = 0
for i in a:
    if i + X >= amax:
        break
    else:
        cnt += 1

print(N - cnt)
