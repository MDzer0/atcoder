N = int(input())
a = list(map(int, input().split()))
a.sort()
rui = [0] * (N + 1)
for i in range(1, N + 1):
    rui[i] = rui[i - 1] + a[i - 1]

cnt = 1
for i in reversed(range(1, N)):
    if 2 * (rui[i]) >= a[i]:
        cnt += 1
    else:
        break

print(cnt)
