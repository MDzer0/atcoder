N, M = map(int, input().split())
ki = [0] * (N + 1)
for i in range(M):
    a, b = map(int, input().split())
    ki[a] += 1
    ki[b] += 1
ans = 'YES'
for i in ki[1:]:
    if i % 2 != 0:
        ans = 'NO'
        break
print(ans)
